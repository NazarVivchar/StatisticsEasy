import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HClasterComponent } from './h-claster.component';

describe('HClasterComponent', () => {
  let component: HClasterComponent;
  let fixture: ComponentFixture<HClasterComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HClasterComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HClasterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
