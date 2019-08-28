import { TestBed } from '@angular/core/testing';

import { InitnumService } from './initnum.service';

describe('InitnumService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: InitnumService = TestBed.get(InitnumService);
    expect(service).toBeTruthy();
  });
});
