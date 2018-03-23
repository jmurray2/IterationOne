import { Component } from '@angular/core';
import { AlertController } from "ionic-angular";
import { NavController, NavParams } from 'ionic-angular';
import { Http ,HttpModule} from '@angular/http';
import { HttpHeaders } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { Headers } from '@angular/http';
import { HTTP } from '@ionic-native/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
@Component({
  selector: 'emergency-page-ionic',
  templateUrl: 'emergency-page.html'
})
export class EmergencyPage {
  films: Observable<any>;
  result = "hey";
  body = {};
  constructor(private http: Http,private httpClient: HttpClient,private alertCtrl: AlertController, public navCtrl: NavController, public navParams: NavParams) {
    
  }

  public callDrone()
  {/*
    let alert = this.alertCtrl.create({
      message: "Are you sure you want to send a drone to this location?",
      buttons: [
        {
          text: 'Yes',
          handler: data => {
            console.log("You have called drone.");
            this.http.get('http://ionic.io', {})
            .subscribe(data => {

              console.log(data.status);
              console.log(data.data); // data received by server
              console.log(data.headers);

            })
            .catch(error => {

              console.log(error.status);
              console.log(error.error); // error message as string
              console.log(error.headers);

            });
            alert.present();
        }
      }],
    })
    */

/*
   let headers =  {headers: new  HttpHeaders({ 'Content-Type': 'application/x-www-form-urlencoded'})};
   let reqOpts = {
    headers: new HttpHeaders()
   };
   this.http.get('http://ionic.io', ({reqOpts}))
			.subscribe(data => {
				console.log(data);
			});
  }

*/
    //let url = 'https://swapi.co/api/films';
    let url = 'http://10.141.166.89:8000/gui/'
    //JSONObject json = new JSONObject();
    //let headers =  {headers: new  HttpHeaders({ "Content-Type": "application/json",})};
    let headers = new Headers();
    headers.append("Content-Type","application/json");
    let result = "";
    this.body = {
      username : "Jon",
      password: "test"
    };
    this.films = this.http.post('/api',{
      username : "Jon",
      password: "test"
    },{headers:headers});
    this.films
    .map(res => res.json)
    .subscribe(data => {
      console.log('my data: ', data);
      console.log('result ' , result);
    });

  }
}