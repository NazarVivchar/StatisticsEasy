import {Component, HostListener, Inject, OnInit} from '@angular/core';
import { DOCUMENT } from '@angular/common';
import {animate, state, style, transition, trigger} from '@angular/animations';


@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent implements OnInit {
  private hover = false;
  private  visibility = 'hidden';

  constructor() { }

  ngOnInit() {
  }

  hideDropdown() {
    this.hover = false;
    this.visibility = 'hidden';
    console.log(1);
  }

  showDropdown() {
    this.hover = true;
    this.visibility = 'visible';
    console.log(2);
  }


}
