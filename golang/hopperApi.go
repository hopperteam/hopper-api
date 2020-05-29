package golang

import (
	"bytes"
	"crypto/rand"
	"crypto/rsa"
	"crypto/x509"
	"encoding/base64"
	"encoding/json"
	"encoding/pem"
	"errors"
	"io/ioutil"
	"net/http"
)

type HopperApiDefinition struct {
	baseUrl      string
	subscribeUrl string
}

type HopperApi struct {
	HopperApiDefinition
}

type NotificationUpdate struct {
	Heading *string
	Timestamp *int64
	ImageUrl *string
	IsDone *bool
	IsSilent *bool
	Content *string
	Actions *[]Action
}

type versionResponse struct {
	Version string `json:"version"`
	Type    string `json:"type"`
}

type apiError struct {
	Reason string `json:"reason"`
}

type apiResponse struct {
	Status string `json:"status"`
}

type apiIdResponse struct {
	apiResponse
	Id string `json:"Id"`
}

type postAppRequest struct {
	Name string `json:"name"`
	ImageUrl string `json:"imageUrl"`
	IsHidden bool `json:"isHidden"`
	BaseUrl string `json:"baseUrl"`
	ManageUrl string `json:"manageUrl"`
	ContactEmail string `json:"contactEmail"`
	Cert string `json:"cert"`
}

type postNotificationRequest struct {
	SubscriptionId string `json:"subscriptionId"`
	Notification *Notification `json:"notification"`
}

type updateNotificationRequest struct {
	Id string `json:"id"`
	Notification map[string]interface{} `json:"notification"`
}

func StrPtr(s string) *string {
	return &s
}

func IntPtr(i int64) *int64 {
	return &i
}

func BoolPtr(b bool) *bool {
	return &b
}

func createKey() (*rsa.PrivateKey, error) {
	return rsa.GenerateKey(rand.Reader, 2048)
}

func encodeKey(key *rsa.PublicKey) string {
	return base64.StdEncoding.EncodeToString(pem.EncodeToMemory(
		&pem.Block{
			Type: "RSA PUBLIC KEY",
			Bytes: x509.MarshalPKCS1PublicKey(key),
	}))
}

func apiPlainRequest(method string, url string, result interface{}) error {
	req, err := http.NewRequest(method, url, nil)
	if err != nil {
		return err
	}

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return err
	}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return err
	}

	if resp.StatusCode != http.StatusOK {
		apiErr := &apiError{}
		err = json.Unmarshal(body, apiErr)
		if err != nil {
			return errors.New("unknown error")
		}
		return errors.New(apiErr.Reason)
	}

	err = json.Unmarshal(body, result)
	return err
}

func apiJsonRequest(method string, url string, reqBody interface{}, result interface{}) error {
	data, err := json.Marshal(reqBody)

	if err != nil {
		return err
	}

	req, err := http.NewRequest(method, url, bytes.NewBuffer(data))
	if err != nil {
		return err
	}

	req.Header.Set("Content-Type", "application/json; charset=utf-8")
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return err
	}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return err
	}

	if resp.StatusCode != http.StatusOK {
		apiErr := &apiError{}
		err = json.Unmarshal(body, apiErr)
		if err != nil {
			return errors.New("unknown error")
		}
		return errors.New(apiErr.Reason)
	}

	err = json.Unmarshal(body, result)
	return err
}

var HopperProd = HopperApiDefinition{"https://api.hoppercloud.net/v1", "https://app.hoppercloud.net/subscribe"}
var HopperDev = HopperApiDefinition{"https://api-dev.hoppercloud.net/v1", "https://dev.hoppercloud.net/subscribe"}

func CreateHopperApi(apiDef HopperApiDefinition) *HopperApi {
	return &HopperApi{HopperApiDefinition: apiDef}
}

func (api *HopperApi) DeserializeApp(data string) (*App, error) {
	app := &App{}
	err := json.Unmarshal([]byte(data), app)
	app.api = api
	return app, err
}

func (api *HopperApi) CheckConnectivity() (bool, error) {
	respObj := &versionResponse{}
	err := apiPlainRequest(http.MethodGet, api.baseUrl + "/", respObj)

	return err == nil, err
}

func (api *HopperApi) CreateApp(name string, baseUrl string, imageUrl string, manageUrl string, contactEmail string) (*App, error) {
	key, err := createKey()
	if err != nil {
		return nil, err
	}

	certStr := encodeKey(&key.PublicKey)

	reqBody := postAppRequest{
		Name: name,
		BaseUrl: baseUrl,
		ImageUrl: imageUrl,
		ManageUrl: manageUrl,
		ContactEmail: contactEmail,
		Cert: certStr,
	}

	apiResp := &apiIdResponse{}
	err = apiJsonRequest(http.MethodPost, api.baseUrl + "/app", reqBody, apiResp)

	if err != nil {
		return nil, err
	}

	return &App{api: api, Id: apiResp.Id, PrivateKey: key}, nil
}

func (api *HopperApi) PostNotification(subscriptionId string, notification *Notification) (string, error) {
	data := postNotificationRequest{
		SubscriptionId: subscriptionId,
		Notification: notification,
	}
	apiResp := &apiIdResponse{}
	err := apiJsonRequest(http.MethodPost, api.baseUrl + "/notification", data, apiResp)

	if err != nil {
		return "", err
	}

	return apiResp.Id, nil
}

func (api *HopperApi) UpdateNotification(notificationId string, params *NotificationUpdate) error {
	update := make(map[string]interface{})

	if params.Heading != nil {
		update["heading"] = params.Heading
	}

	if params.Timestamp != nil {
		update["timestamp"] = params.Timestamp
	}

	if params.ImageUrl != nil {
		update["imageUrl"] = params.ImageUrl
	}

	if params.IsDone != nil {
		update["isDone"] = params.IsDone
	}

	if params.IsSilent != nil {
		update["isSilent"] = params.IsSilent
	}

	if params.Content != nil {
		update["content"] = params.Content
	}

	if params.Actions != nil {
		update["actions"] = params.Actions
	}

	data := updateNotificationRequest{
		Id:      notificationId,
		Notification: update,
	}
	apiResp := &apiResponse{}
	return apiJsonRequest(http.MethodPut, api.baseUrl + "/notification", data, apiResp)
}

func (api *HopperApi) DeleteNotification(notificationId string) error {
	return apiPlainRequest(http.MethodDelete, api.baseUrl + "/app?Id=" + notificationId, &apiResponse{})
}
