import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RunMovAvgComponent } from './run-mov-avg.component';

describe('RunMovAvgComponent', () => {
  let component: RunMovAvgComponent;
  let fixture: ComponentFixture<RunMovAvgComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RunMovAvgComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RunMovAvgComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
