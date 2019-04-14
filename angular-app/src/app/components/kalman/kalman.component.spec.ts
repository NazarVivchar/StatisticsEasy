import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KalmanComponent } from './kalman.component';

describe('KalmanComponent', () => {
  let component: KalmanComponent;
  let fixture: ComponentFixture<KalmanComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KalmanComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KalmanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
