import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';
import { AlertController } from 'ionic-angular';
import { LoginPage } from '../login-page/login-page';
// import { Http } from 'ionic-angular';
import { Events } from 'ionic-angular';

@Component({
  selector: 'user-page-ionic',
  templateUrl: 'user-page.html'
})
export class UserPage{
    user: {firstName:string , lastName:string , addresses: Array<string> , billingInfo: string };
    constructor(private alertCtrl: AlertController, public navCtrl: NavController, public navParams: NavParams, private events: Events) {
        this.user = ({
            firstName: 'Jon',
            lastName: 'Murray',
            addresses: new Array("1234 Street City"),
            billingInfo: '98765'
        });
		console.log("Subbed");
		events.subscribe("deleteAccount", eventData => {
			console.log("hmm")
			this.deleteAccount(true);
		});
    }

    public addAddress()
    {
        let alert = this.alertCtrl.create({
            title: 'Add Address',
            inputs: [
                {
                    name: 'Street',
                    placeholder: 'Street'
                },
                {
                    name: 'City',
                    placeholder: 'City'
                },
                {
                    name: 'State',
                    placeholder: 'State'
                },
                {
                    name: 'Zip',
                    placeholder: 'Zip'
                }
            ],
            buttons: [
                {
                    text: 'Save',
                    handler: data => {
                        this.user.addresses.push(data.Street + " " + data.City + " " + data.State + " " + data.Zip);
						// this.http.put("/user", {}) // The user.put is definitely not in its final version. I don't know what structure it will end up taking.
                    }
                },
                {
                    text: 'Cancel',
                    role: 'cancel'
                }
            ]
        });
        
        alert.present();
    }

    public signOut()
    {
        let alert = this.alertCtrl.create({
            message: "Are you sure you want to sign out?",
            buttons: [
                {
                    text: 'Yes',
                    handler: data => {
                        this.navCtrl.setRoot(LoginPage)
                    }
                },
                {
                    text: 'No',
                    role: 'cancel'
                }
            ]
        });
        alert.present();
    }

    public deleteAccount(force=false) // Force just deletes the account without a button. Used for testing.
    {
		const that = this;
		console.log("WTF")
		function deleteAction()
		{
			//http.delete("/user", {}) // This is blue in a bad way. Also the server.py isn't deleting enough from the database.
			that.events.publish("deleteAccount:status", "failure")
		}
		
		if(force) 
		{
			deleteAction()
		}
		else 
		{
			let alert = this.alertCtrl.create({
				message: "Are you sure you want to delete your account? You will no longer be able to sign in.",
				buttons: [
					{
						text: 'Yes',
						handler: data => {
							deleteAction()
							this.navCtrl.setRoot(LoginPage)
						}
					},
					{
						text: 'No',
						role: 'cancel'
					}
				]
			});
			alert.present();
		}
    }
}