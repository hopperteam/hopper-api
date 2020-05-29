package main

import (
	"fmt"
	hopperApi "github.com/hopperteam/hopper-api/golang"
)

func main() {
	api := hopperApi.CreateHopperApi(hopperApi.HopperDev)
	//app, _ := api.CreateApp("123", "123", "123", "manage", "contact")
	//subR, _ := app.CreateSubscribeRequest("http://localhost", nil)
	//fmt.Printf(subR)
	ok, err := api.CheckConnectivity()
	fmt.Println(ok)
	fmt.Println(err)
	if err != nil {
		return
	}

	//app, err := api.CreateApp("Hopper", "https://hoppercloud.net", "https://hoppercloud.net/logo.png", "https://hoppercloud.net/manageSubscription", "info@hoppercloud.net")
	app, err := api.DeserializeApp("{\"Id\":\"5ecac655a9c121e4ba12f580\",\"PrivateKey\":{\"N\":24482052357113577494650785097946731170764521797076544399595017554141641847351299850041031182980285905228288112598211237645087566703698975256357646031276778026949710616179465496762812237826803149695611517050093534948401567660459389839904706714597777387979648261563444732422848640055297225005171397504016634977323962707307281101465698143821620948281282010782244928676756079363935347746348381327310991174992007738348043727045474535129172716503345006163972017127814380181252031729206685026934987082436099060593899702933324960171812030751959366324336246481488675778407130133437910073839898244049391783544289174007444943963,\"E\":65537,\"D\":2598115173775499816520381011584593669113130736815346541635768300182417856299926613318207606048917229517108561928690040096763416488765527456367661445405343411774039662107331469703913195814355492410897326717478684339626972596830722436738594003387819731348680190719345684331002522110938739947067565949622895406642211338184461899396599532378036258073051036707037576303551767097560153002611190463202444140754249620088566162524211693443317293263267239774378826673883209016513094560172275473089513638551111425872708089993605813336837907057573126655566120477112213546332941025603016898741646547052667224107392976350316531473,\"Primes\":[161508652300879908264662845622469244134922723078356659756423182348475918461591596371654438347624647761186632430497580359236519532256252749475396106039200495600740027405378467186407051798148259103545629061683171091086400050803835170885240069283358852335186577797961322671893278244344773236299885230176604128851,151583534431982860957333852698165040546999720102289183628331148593777222623055909414765311755820090767708591656957777460839499273593642207358099252033792336152730742182920896822574311225377100989770100965633914589623680000820565604263562483782097740167013225808525484814911208101186911593063783743820676253913],\"Precomputed\":{\"Dp\":76331980352586390567002868308136813827839181296504557414826001343694296327713171277532150897650576617101709765510048583960082945391232016452552283266829365865653319634011209585909822274376980598337157858256779244935077210943405871233035169537555229751591758254330439422604367003987594888706419963066514126173,\"Dq\":120971695650725049877023287056463187980670146036436347134122339041331405124297269850787422913055257142266120830099114649081091459900432957401823505498747375764226670089432362567927760283651572943023876904719242578489978354256637048296273021755211193771688141603025770279223736303283303326982040944341501891025,\"Qinv\":59330035298166945364286189142324951116259778549444880134691469255871775192913700541882621453948850044743616714108657573564060985777915065853572895359942439844332843468259747342622924468091757984534361269368867164058885014769230606729787659273007423792294975962024021878439225918400914434538446735677950808760,\"CRTValues\":[]}}}\n")
	if err != nil {
		// An error occured :(
		fmt.Println(err)
		return
	}

	accName := "TestUser"
	url, err := app.CreateSubscribeRequest("https://my-callback.com", &accName)
	if err != nil {
		// An error occured :(
		return
	}
	fmt.Println(url)

	fmt.Println(app)
	ser, err := app.Serialize()
	if err != nil {
		// An error occured :(
		fmt.Println(err)
		return
	}

	fmt.Println(ser)

	//fmt.Println(api.PostNotification("123",
	//	hopperApi.DefaultNotification("Hi", "Test").IsSilent(true).Action(hopperApi.TextAction("Reply", "https://test.com"))),
	//)
}