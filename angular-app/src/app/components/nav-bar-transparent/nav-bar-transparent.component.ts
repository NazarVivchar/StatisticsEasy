import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-nav-bar-transparent',
  templateUrl: './nav-bar-transparent.component.html',
  styleUrls: ['./nav-bar-transparent.component.css']
})
export class NavBarTransparentComponent implements OnInit {
  private hover = new Array(2).fill(false);
  private  visibility = new Array(2).fill('hidden');

  constructor() {
    this.hover.fill(false);
  }

  ngOnInit() {
  }

  hideDropdown(id:number) {
    this.hover[id] = false;
    this.visibility[id] = 'hidden';
    console.log(1);
  }

  showDropdown(id:number) {
    this.hover[id] = true;
    this.visibility[id] = 'visible';
    console.log(2);
  }


}
