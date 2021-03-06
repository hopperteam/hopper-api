package golang

import (
	"crypto/rsa"
	"encoding/json"
	"github.com/dgrijalva/jwt-go"
	"net/http"
)

// Represents a single app in Hopper
type App struct {
	api        *HopperApi
	Id         string
	PrivateKey *rsa.PrivateKey
}

type subscribeRequest struct {
	jwt.StandardClaims
	Callback       string   `json:"callback"`
	RequestedInfos []string `json:"requestedInfos"`
	AccountName    *string  `json:"accountName"`
}

// Params to update an app
type AppUpdateParams struct {
	Name *string
	ImageUrl *string
	ManageUrl *string
	ContactEmail *string
	cert *string
}

type updateAppRequest struct {
	Id string `json:"id"`
	Content string `json:"content"`
}

// Updates the app's metadata at Hopper
func (app *App) Update(params *AppUpdateParams) error {
	update := jwt.MapClaims{}

	if params.Name != nil {
		update["name"] = params.Name
	}

	if params.ImageUrl != nil {
		update["imageUrl"] = params.ImageUrl
	}

	if params.ManageUrl != nil {
		update["manageUrl"] = params.ManageUrl
	}

	if params.ContactEmail != nil {
		update["contactEmail"] = params.ContactEmail
	}

	if params.cert != nil {
		update["cert"] = params.cert
	}

	encUpdate, err := jwt.NewWithClaims(jwt.SigningMethodRS256, update).SignedString(app.PrivateKey)
	if err != nil {
		return err
	}

	data := updateAppRequest{
		Id:      app.Id,
		Content: encUpdate,
	}
	apiResp := &apiResponse{}
	return apiJsonRequest(http.MethodPut, app.api.baseUrl + "/app", data, apiResp)
}

// Generates new keys for this App and update them at Hopper
func (app *App) GenerateNewKeys() error {
	key, err := createKey()
	if err != nil {
		return err
	}

	certStr := encodeKey(&key.PublicKey)
	err = app.Update(&AppUpdateParams{
		cert: &certStr,
	})

	if err != nil {
		return err
	}

	app.PrivateKey = key
	return nil
}

// Create a subscription request
func (app *App) CreateSubscribeRequest(callback string, accountName *string) (string, error) {
	subReq := subscribeRequest{
		StandardClaims: jwt.StandardClaims{},
		Callback:       callback,
		RequestedInfos: make([]string, 0),
		AccountName:    accountName,
	}

	encSubReq, err := jwt.NewWithClaims(jwt.SigningMethodRS256, subReq).SignedString(app.PrivateKey)
	if err != nil {
		return "", nil
	}
	return app.api.subscribeUrl +
		"?id=" + app.Id + "&content=" + encSubReq, nil

}

// Serialize this App into a JSON-String
func (app *App) Serialize() (string, error) {
	data, err := json.Marshal(app)
	if err != nil {
		return "", err
	}
	return string(data), nil
}
