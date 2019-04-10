import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MovAvgComponent } from './mov-avg.component';

describe('MovAvgComponent', () => {
  let component: MovAvgComponent;
  let fixture: ComponentFixture<MovAvgComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MovAvgComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MovAvgComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
