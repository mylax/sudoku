import { TestBed } from '@angular/core/testing';

import { IdsService } from './ids.service';

describe('IdsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: IdsService = TestBed.get(IdsService);
    expect(service).toBeTruthy();
  });
});
