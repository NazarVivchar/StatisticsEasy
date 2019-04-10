import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DisributionsComponent } from './disributions.component';

describe('DisributionsComponent', () => {
  let component: DisributionsComponent;
  let fixture: ComponentFixture<DisributionsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DisributionsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DisributionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
