import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ExpMovAvgComponent } from './exp-mov-avg.component';

describe('ExpMovAvgComponent', () => {
  let component: ExpMovAvgComponent;
  let fixture: ComponentFixture<ExpMovAvgComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ExpMovAvgComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ExpMovAvgComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
