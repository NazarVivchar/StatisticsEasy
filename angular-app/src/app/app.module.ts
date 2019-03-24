import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TestComponent } from './components/test/test.component';
import { FileUploadModule } from 'ng2-file-upload';
import { ChartsModule } from 'ng2-charts';
import { ChartComponent } from './components/chart/chart.component';
import { HighchartComponent } from './components/highchart/highchart.component';
// import { HighChartComponent } from './components/high-chart/high-chart.component';
import { HighchartsChartModule } from 'highcharts-angular';
import { MainPageComponent } from './components/main-page/main-page.component';
import { MainRegChartComponent } from './components/main-reg-chart/main-reg-chart.component';
import { MainDnnChartComponent } from './components/main-dnn-chart/main-dnn-chart.component';
import { RegChartComponent } from './components/reg-chart/reg-chart.component';
import { RegDnnComponent } from './components/reg-dnn/reg-dnn.component';
import {RouterModule, Routes} from '@angular/router';
import {NavBarComponent} from './components/nav-bar/nav-bar.component';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FooterComponent } from './components/footer/footer.component';
import { AccordionComponent } from './components/accordion/accordion.component';

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
    AccordionComponent
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
    BrowserAnimationsModule



  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
