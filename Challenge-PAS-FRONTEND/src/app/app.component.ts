import {Component, OnInit} from '@angular/core';
import {SpeechToTextService} from "./services/speech-to-text.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  record:boolean=false;
  transcript: boolean=false;
  transcriptionResult:any;

  constructor(private speechToText:SpeechToTextService) {}

  public ngOnInit(): void {}

  recording(){
    this.record=true;
    //this.transcriptionResult=''
    this.enregistrer();
  }

  enregistrer(){
    this.speechToText.enregistrement().subscribe(data => {
      this.record=false;
      this.transcript=true;
      this.transcription();
      console.log(data);
    }, err => {
      console.log(err);
    });
  }

  transcription(){
    this.speechToText.transcription().subscribe(data => {
      this.transcript = false;
      this.transcriptionResult = data;
      console.log(data);
    }, err => {
      console.log(err);
    });
  }

}
