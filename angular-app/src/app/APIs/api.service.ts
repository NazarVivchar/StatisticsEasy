import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseurl = 'http://127.0.0.1:8000';
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json', 'Accept':'application/json'});
  constructor(private http: HttpClient) {
  }
  getDemoRegression(): Observable<any> {
    return this.http.get(this.baseurl + '/regression_demo_info/',
      {headers: this.httpHeaders});
  }
  getDemoDnn(): Observable<any> {
    return this.http.get(this.baseurl + '/dnn_demo_info/',
      {headers: this.httpHeaders});
  }
  getRegression(): Observable<any> {
    return this.http.get(this.baseurl + '/regression_info/',
      {headers: this.httpHeaders});
  }
  getDnn(): Observable<any> {
    return this.http.get(this.baseurl + '/dnn_info/',
      {headers: this.httpHeaders});
  }

  getPolynomial(): Observable<any> {
    return this.http.get(this.baseurl + '/poly_info/',
      {headers: this.httpHeaders});
  }

  getLogistical(): Observable<any> {
    return this.http.get(this.baseurl + '/log_info/',
      {headers: this.httpHeaders});
  }
  getMovingAverages(): Observable<any> {
    return this.http.get(this.baseurl + '/simple_ma_info/',
      {headers: this.httpHeaders});
  }
  getExpMovingAverages(): Observable<any> {
    return this.http.get(this.baseurl + '/exp_ma_info/',
      {headers: this.httpHeaders});
  }
  getWeightMovingAverages(): Observable<any> {
    return this.http.get(this.baseurl + '/weighted_ma_info/',
      {headers: this.httpHeaders});
  }
  getRunningMovingAverages(): Observable<any> {
    return this.http.get(this.baseurl + '/running_ma_info/',
      {headers: this.httpHeaders});
  }
  getHCluster(): Observable<any> {
    return this.http.get(this.baseurl + '/h_claster_info/',
      {headers: this.httpHeaders});
  }
  getTSNA(): Observable<any> {
    return this.http.get(this.baseurl + '/t_sn/',
      {headers: this.httpHeaders});
  }
  getKMeans(): Observable<any> {
    return this.http.get(this.baseurl + '/k_means_info/',
      {headers: this.httpHeaders});
  }

  sendDistributionData(data): Observable<any> {
    return this.http.post(this.baseurl + '/distribution_info/',
      data,{headers: this.httpHeaders});
  }
  getDistributionData(httpParams:HttpParams): Observable<any> {
    return this.http.get(this.baseurl + '/distribution_info/',
      {params: httpParams,headers: this.httpHeaders });
  }
}
