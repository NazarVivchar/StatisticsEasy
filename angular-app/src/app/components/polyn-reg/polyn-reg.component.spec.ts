import {async, ComponentFixture, TestBed} from '@angular/core/testing';

import {PolynRegComponent} from './polyn-reg.component';

describe('PolynRegComponent', () => {
  let component: PolynRegComponent;
  let fixture: ComponentFixture<PolynRegComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [PolynRegComponent]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PolynRegComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
