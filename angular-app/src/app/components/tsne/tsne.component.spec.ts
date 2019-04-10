import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TSneComponent } from './tsne.component';

describe('TSneComponent', () => {
  let component: TSneComponent;
  let fixture: ComponentFixture<TSneComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TSneComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TSneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
