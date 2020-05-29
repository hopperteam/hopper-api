package main

import (
	"fmt"
	hopperApi "github.com/hopperteam/hopper-api/golang"
)

func main() {
	api := hopperApi.CreateHopperApi(hopperApi.HopperDev)

	ok, _ := api.CheckConnectivity()
	if !ok {
		fmt.Println("Could not connect!")
		return
	}

	app, err := api.CreateApp("Hopper", "http://localhost", "https://hoppercloud.net/logo.png", "https://hoppercloud.net/manageSubscription", "info@hoppercloud.net")
	if err != nil {
		// An error occured :(
		fmt.Println(err)
		return
	}

	err = app.Update(&hopperApi.AppUpdateParams{Name: hopperApi.StrPtr("HopperApp")})
	if err != nil {
		// An error occured :(
		fmt.Println(err)
		return
	}

	err = app.GenerateNewKeys()
	if err != nil {
		// An error occured :(
		fmt.Println(err)
		return
	}

	str, err := app.Serialize()
	if err != nil {
		// An error occured :(
		fmt.Println(err)
		return
	}
	fmt.Println(str)

	url, err := app.CreateSubscribeRequest("https://listener.hoppercloud.net?id=123123", hopperApi.StrPtr("Test User"))
	if err != nil {
		// An error occured :(
		return
	}
	fmt.Println(url)

	id, err := api.PostNotification("key",
		hopperApi.DefaultNotification("TestTest", "this is the body").IsDone(false).Action(hopperApi.TextAction("Reply", "https://test.com")),
	)
	if err != nil {
		// An error occured :(
		return
	}

	err = api.UpdateNotification(id, &hopperApi.NotificationUpdate{Heading: hopperApi.StrPtr("Updated")})
	if err != nil {
		// An error occured :(
		return
	}

	err = api.DeleteNotification(id)
	if err != nil {
		// An error occured :(
		return
	}
}
