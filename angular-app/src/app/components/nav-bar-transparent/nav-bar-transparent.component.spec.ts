import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NavBarTransparentComponent } from './nav-bar-transparent.component';

describe('NavBarTransparentComponent', () => {
  let component: NavBarTransparentComponent;
  let fixture: ComponentFixture<NavBarTransparentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NavBarTransparentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NavBarTransparentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
