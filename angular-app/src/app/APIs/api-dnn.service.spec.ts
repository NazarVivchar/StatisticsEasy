import {TestBed} from '@angular/core/testing';

import {ApiDnnService} from './api-dnn.service';

describe('ApiDnnService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ApiDnnService = TestBed.get(ApiDnnService);
    expect(service).toBeTruthy();
  });
});
