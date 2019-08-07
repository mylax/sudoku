import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css']
})
export class BoardComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }
  setInputFilter(textbox, inputFilter) {
    ["input", "keydown", "keyup", "mousedown", "mouseup", "select", "contextmenu", "drop"].forEach(function(event) {
      textbox.addEventListener(event, function() {
        if (inputFilter(this.value)) {
          this.oldValue = this.value;
          this.oldSelectionStart = this.selectionStart;
          this.oldSelectionEnd = this.selectionEnd;
        } else if (this.hasOwnProperty("oldValue")) {
          this.value = this.oldValue;
          this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
        }
      });
    });
  };
  create_square() {
    if (document.getElementById("board").children.length == 0) {
      for (let i = 1; i <= 9; i++) {
          var elem = document.createElement('div');
          elem.className = "bigsquare";
          elem.id = "test".concat(String(i));
          // elem.type = "text";
          for (let j = 1;j <= 9; j++) {
              var smallsquare = document.createElement('input');
              smallsquare.className = "smallsquare";
              smallsquare.id = String(j + 9 * (i - 1));
              smallsquare.type = "text";
              smallsquare.name = "testing" + (j + 9 * (i - 1));
              this.setInputFilter(smallsquare, function(value) {
                return /^\d*$/.test(value) && (value === "" || parseInt(value) <= 9); });
              elem.appendChild(smallsquare);
          }
          document.getElementById("board").appendChild(elem);
      }
    };
  };
}
