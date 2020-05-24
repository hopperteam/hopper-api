package golang

import (
	"crypto/rsa"
	"encoding/json"
	"github.com/dgrijalva/jwt-go"
)

type App struct {
	api        *HopperApi
	Id         string
	PrivateKey *rsa.PrivateKey
}

type SubscribeRequest struct {
	jwt.StandardClaims
	Callback       string   `json:"callback"`
	RequestedInfos []string `json:"requestedInfos"`
	AccountName    *string  `json:"accountName"`
}

func (app *App) CreateSubscribeRequest(callback string, accountName *string) (string, error) {
	subReq := SubscribeRequest{
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
		"?Id=" + app.Id + "&content=" + encSubReq, nil

}

func (app *App) Serialize() (string, error) {
	data, err := json.Marshal(app)
	if err != nil {
		return "", err
	}
	return string(data), nil
}
