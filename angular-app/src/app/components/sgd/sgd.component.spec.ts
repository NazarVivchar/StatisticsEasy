import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SGDComponent } from './sgd.component';

describe('SGDComponent', () => {
  let component: SGDComponent;
  let fixture: ComponentFixture<SGDComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SGDComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SGDComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
