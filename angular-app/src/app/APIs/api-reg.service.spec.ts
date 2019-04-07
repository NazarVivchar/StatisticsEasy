import {TestBed} from '@angular/core/testing';

import {ApiRegService} from './api-reg.service';

describe('ApiRegService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ApiRegService = TestBed.get(ApiRegService);
    expect(service).toBeTruthy();
  });
});
