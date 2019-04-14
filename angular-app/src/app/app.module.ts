import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {TestComponent} from './components/test/test.component';
import {FileUploadModule} from 'ng2-file-upload';
import {ChartsModule} from 'ng2-charts';
import {ChartComponent} from './components/chart/chart.component';
import {HighchartComponent} from './components/highchart/highchart.component';
// import { HighChartComponent } from './components/high-chart/high-chart.component';
import {HighchartsChartModule} from 'highcharts-angular';
import {MainPageComponent} from './components/main-page/main-page.component';
import {MainRegChartComponent} from './components/main-reg-chart/main-reg-chart.component';
import {MainDnnChartComponent} from './components/main-dnn-chart/main-dnn-chart.component';
import {RegChartComponent} from './components/reg-chart/reg-chart.component';
import {RegDnnComponent} from './components/reg-dnn/reg-dnn.component';
import {RouterModule} from '@angular/router';
import {NavBarComponent} from './components/nav-bar/nav-bar.component';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {FooterComponent} from './components/footer/footer.component';
import {AccordionComponent} from './components/accordion/accordion.component';
import {PolynRegComponent} from './components/polyn-reg/polyn-reg.component';
import {LogRegComponent} from './components/log-reg/log-reg.component';
import { MovAvgComponent } from './components/mov-avg/mov-avg.component';
import { NavBarTransparentComponent } from './components/nav-bar-transparent/nav-bar-transparent.component';
import { ExpMovAvgComponent } from './components/exp-mov-avg/exp-mov-avg.component';
import { RunMovAvgComponent } from './components/run-mov-avg/run-mov-avg.component';
import { WeightMovAvgComponent } from './components/weight-mov-avg/weight-mov-avg.component';
import { DisributionsComponent } from './components/disributions/disributions.component';
import {FormsModule} from "@angular/forms";
import { KMeansComponent } from './components/kmeans/kmeans.component';
import { HClasterComponent } from './components/h-claster/h-claster.component';
import {TSneComponent} from "./components/tsne/tsne.component";
import { KalmanComponent } from './components/kalman/kalman.component';
import { TreeComponent } from './components/tree/tree.component';
import { SGDComponent } from './components/sgd/sgd.component';
import { SVMComponent } from './components/svm/svm.component';
import { GeneralComponent } from './components/general/general.component';

@NgModule({
  declarations: [
    AppComponent,
    TestComponent,
    ChartComponent,
    HighchartComponent,
    MainPageComponent,
    MainRegChartComponent,
    MainDnnChartComponent,
    RegChartComponent,
    RegDnnComponent,
    NavBarComponent,
    FooterComponent,
    AccordionComponent,
    PolynRegComponent,
    LogRegComponent,
    MovAvgComponent,
    NavBarTransparentComponent,
    ExpMovAvgComponent,
    RunMovAvgComponent,
    WeightMovAvgComponent,
    DisributionsComponent,
    KMeansComponent,
    HClasterComponent,
    TSneComponent,
    KalmanComponent,
    TreeComponent,
    SGDComponent,
    SVMComponent,
    GeneralComponent
  ],
  imports: [
    // BsDropdownModule.forRoot(),
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FileUploadModule,
    ChartsModule,
    HighchartsChartModule,
    RouterModule,
    NgbModule,
    BrowserAnimationsModule,
    FormsModule


  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
