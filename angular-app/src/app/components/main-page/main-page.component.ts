import {Component, HostListener, Inject, OnInit} from '@angular/core';
import {animate, state, style, transition, trigger} from '@angular/animations';
import {DOCUMENT} from '@angular/common';

declare function headerMethod(): any;
@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css'],
  animations: [
  trigger('blink', [
  state('start', style({opacity: 1})),
  state('end', style({opacity: 0.3})),
  transition('* <=> *', animate('1s ease-out')),
]),
    trigger('visibilityChanged', [
      state('shown', style({opacity: 1})),
      state('hidden', style({opacity: 0})),
      state('true', style({opacity: 1})),
      state('false', style({opacity: 0})),
      transition('shown => hidden', animate('0.3s')),
      transition('hidden => shown', animate('0.7s')),
      transition('false => true', animate('1.5s'))
    ]),
    trigger(
      'enterAnimationLeft', [
        transition(':enter', [
          style({transform: 'translateX(-100%)', opacity: 0}),
          animate('2s ease-in', style({transform: 'translateX(0)', opacity: 1 }))
        ]),
        transition(':leave', [
          style({transform: 'translateX(0)', opacity: 1}),
          animate('2s', style({transform: 'translateX(-100%)', opacity: 0}))
        ])
      ]),
     trigger(
      'enterAnimationRight', [
        transition(':enter', [
          style({transform: 'translateX(100%)', opacity: 0}),
          animate('2s ease-in', style({transform: 'translateX(0)', opacity: 1}))
        ]),
        transition(':leave', [
          style({transform: 'translateX(0)', opacity: 1}),
          animate('2s', style({transform: 'translateX(100%)', opacity: 0}), )
        ])
      ]),
    trigger(
      'enterAnimationTop', [
        transition(':enter', [
          style({transform: 'translateY(-100%)', opacity: 0}),
          animate('2.5s ease-in', style({transform: 'translateY(0)', opacity: 1}))
        ]),
        transition(':leave', [
          style({transform: 'translateY(0)', opacity: 1}),
          animate('2.5s', style({transform: 'translateY(-100%)', opacity: 0}))
        ])
      ]),
    trigger(
      'enterAnimationBottom', [
        transition(':enter', [
          style({transform: 'translateY(100%)', opacity: 0}),
          animate('2s ease-in-out', style({transform: 'translateY(0)', opacity: 1}))
        ]),
        transition(':leave', [
          style({transform: 'translateY(0)', opacity: 1}),
          animate('1.5s', style({transform: 'translateX(100%)', opacity: 0}))
        ])
      ])
    ]
})
export class MainPageComponent implements OnInit {
  private ttHidden = true;
  private hover = false;
  private  visibility = 'hidden';
  private navVisibility = 'shown';
  private state1 = 'start';
  private state2 = 'start';
  private interval;
  private anchorsReached: boolean[];
  private anchorsNumber: number;
  private methodName: string[];
  private methodUrl: string[];
 private allReached = false;
  constructor(@Inject(DOCUMENT) document) {
    // this.anchorsNumber = 5;
    this.anchorsNumber = 13;
    this.anchorsReached = new Array(this.anchorsNumber).fill(false);

  }

  ngOnInit() {



    this.interval = setInterval(() => {
      setTimeout(() => this.state2 = this.onDone(this.state2), 500);
      this.state1 = this.onDone(this.state1);
    }, 1400);

  }

  onDone(states: string) {
      return states === 'start' ? 'end' : 'start';
    }
    @HostListener('window:scroll', ['$event'])
  onWindowScroll(e) {

     const scrollposition = window.pageYOffset;
     if (scrollposition > document.documentElement.clientHeight) {
       const navbar = document.getElementById('navbar');
       const drop = document.getElementById('drop');
       navbar.classList.remove('nav-transparent');
       navbar.classList.add('nav-colored');
       this.navVisibility = 'shown';
       drop.classList.remove('drop-transparent');
       drop.classList.add('drop-colored');
     } else if (scrollposition > 0.08 * document.documentElement.clientHeight &&
       window.pageYOffset < document.documentElement.clientHeight) {
       const navbar = document.getElementById('navbar');
       const drop = document.getElementById('drop');
       navbar.classList.remove('nav-transparent');
       navbar.classList.remove('nav-colored');
       this.navVisibility = 'hidden';
     } else {
       const navbar = document.getElementById('navbar');
       const drop = document.getElementById('drop');
       navbar.classList.remove('nav-colored');
       navbar.classList.add('nav-transparent');
       this.navVisibility = 'shown';
       drop.classList.remove('drop-colored');
       drop.classList.add('drop-transparent');
     }
      if (scrollposition > 2.5 * document.documentElement.clientHeight) {
        this.ttHidden = false;
      } else {
        this.ttHidden = true;
      }
      // this.allReached = true;
      // if (!this.allReached) {
      for (let i = 0; i < this.anchorsNumber; ++i) {
        const bool = (document.documentElement.scrollTop > document.getElementById('anchor' + (i + 1)).getBoundingClientRect().top + 300 * i);
         this.allReached = this.allReached && bool;
        if (!this.anchorsReached[i]) {
          this.anchorsReached[i] = bool;
        }
      }
  }

   offset(el) {
    const rect = el.getBoundingClientRect();
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    return { top: rect.top + scrollTop};
}

  hideDropdown() {
    this.hover = false;
    this.visibility = 'hidden';
  }

  showDropdown() {
    this.hover = true;
    this.visibility = 'visible';
  }

  toTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: 'smooth'
    });
  }

}
