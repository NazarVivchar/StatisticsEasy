import {Component, HostListener, Inject, OnInit} from '@angular/core';
import { DOCUMENT } from '@angular/common';
import {animate, state, style, transition, trigger} from '@angular/animations';


@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent implements OnInit {
  private hover = new Array(4).fill(false);
  private  visibility = new Array(4).fill('hidden');

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
