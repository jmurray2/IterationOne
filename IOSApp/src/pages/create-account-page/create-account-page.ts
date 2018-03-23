import { Component } from '@angular/core';
import { Events } from 'ionic-angular';
import { NavController, NavParams } from 'ionic-angular';
import { LoginPage } from '../login-page/login-page';
import { AlertController } from "ionic-angular";
// import { Http } from 'ionic-angular';

@Component({
  selector: 'create-account-page-ionic',
  templateUrl: 'create-account-page.html'
})
export class CreateAccountPage {

    constructor(private alertCtrl: AlertController, public navCtrl: NavController, public navParams: NavParams, private events: Events) {
		events.subscribe("createAccount", eventData => {
			this.createAccount(eventData['Username'], eventData['Email'], eventData['Password']);
		});
    }

    public createAccount(username,email,password) 
    {
		this.events.publish("createAccount:status", "success");
		
		/*
		const info = {'Password': password, 'Email': email, 'Username': username};
		this.http.post('/user', info)
			.map(res => res.json())
			.subscribe(data => {
				if(data['status'] == 'success')
				{
					this.events.publish("createAccount:status", "success");
					this.navCtrl.setRoot(LoginPage);
				}
				else // Not sure under what conditions this would occur.
				{
					this.events.publish("createAccount:status", "failure");
					let alert = this.alertCtrl.create({
					message: "An error has occured. Please try again.",
					buttons:[ {
							text: "Ok",
							role: "cancel"
						  }]
					});
					alert.present();
				}
			});
		*/

		let alert = this.alertCtrl.create({
      message: "Your account was created successfully. You may now log in.",
      buttons: [
        {
					text: 'Okay',
					handler: data => {
						this.navCtrl.setRoot(LoginPage);
					}
        }
      ] 
		});
		alert.present();
	}
}