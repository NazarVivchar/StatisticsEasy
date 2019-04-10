import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WeightMovAvgComponent } from './weight-mov-avg.component';

describe('WeightMovAvgComponent', () => {
  let component: WeightMovAvgComponent;
  let fixture: ComponentFixture<WeightMovAvgComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WeightMovAvgComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WeightMovAvgComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
