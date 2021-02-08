#ifndef LOGGER_H
#define LOGGER_H

/** @file logger.h
 *  @brief Logger constants, structures, function prototypes
 *  @author Tsidkeenu Aznar
 *  @date 01Feb2021
 */

#include <cinttypes>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <time.h>
// Default Logger Data Values
#define DTEMP	24.6
#define DHUMID	32
#define DPRESS	1013.5
#define DXA	1
#define DYA	1
#define DZA	1
#define DPITCH	10
#define DROLL	15
#define DYAW	20
#define DXM	1
#define DYM	1
#define DZM	1
#define DLAT	43.7289
#define DLONG	-79.6074
#define DALT	166
#define DSPEED	99
#define DHEADING 320
#define SEARCHSTR "serial\t\t:"
#define SYSINFOBUFSZ 512


typedef struct readings{
time_t	rtime;		///<Reading time
float 	temperature;	///<Degrees Celsius
float 	humidity;		///<Per cent relative humidity
float	pressure;		///<Kilo Pascals
float	xa;			///<X-axis accelaration
float	ya;			///<Y-axis accelaration
float	za;			///<Z-axis accelaration
float	pitch;		///<Pitch angle
float	roll;		///<Roll angle
float	yaw;			///<Yaw angle
float	xm;			///<X axis micro Teslas
float	ym;			///<Y axis micro Teslas
float	zm;			///<Z axis micro Teslas
float	latitude;		///<Latitude
float	longitude;	///<Longitude
float	altitude;		///<Altitude
float	speed;		///<Speed kph
float	heading;		///<Heading degrees True
}reading_s;



uint64_t DlGetSerial(void)
{
	static uint64_t serial = 0;
	FILE * fp;
	char buf[SYSINFOBUFSZ];
	char searchstring[] = SEARCHSTR;
	fp = fopen ("/proc/cpuinfo", "r");
	if (fp != NULL)
	{
		while (fgets(buf, sizeof(buf), fp) != NULL)
		{
			if (!strncasecmp(searchstring, buf, strlen(searchstring)))
			{
				sscanf(buf+strlen(searchstring), "%Lx", &serial);
			}
		}
		fclose(fp);
	}
     if(serial==0)
     {
         system("uname -a");
         system("ls --fu /usr/lib/codeblocks | grep -Po '\\.\\K[^ ]+'>stamp.txt");
         fp = fopen ("stamp.txt", "r");
         if (fp != NULL)
         {
             while (fgets(buf, sizeof(buf), fp) != NULL)
             {
                sscanf(buf, "%Lx", &serial);
             }
             fclose(fp);
        }
     }
	return serial;
}


int DlInitialization(void){

    fprintf(stdout,"Data Logger Initialization\n\n");
    return 0;

}

reading_s	DlGetLoggerReadings(void){

    readings creads = {500,DTEMP,DHUMID,DPRESS,DXA,DYA,DZA,DPITCH,DROLL,DYAW,DXM,DYM,DZM,DLAT,DLONG,DALT,DSPEED,DHEADING};
    /*
    creads.rtime = 500;
    creads.temperature = DTEMP;
    creads.humidity = DHUMID;
    creads.pressure = DPRESS;
    creads.xa = DXA;
    creads.ya = DYA;
    creads.za = DZA;
    creads.pitch = DPITCH;
    creads.roll = DROLL;
    creads.yaw = DYAW;
    creads.xm = DXM;
    creads.ym = DYM;
    creads.zm = DZM;
    creads.latitude = DLAT;
    creads.longitude = DLONG;
    creads.altitude = DALT;
    creads.speed = DSPEED;
    creads.heading = DHEADING;
    */
    return creads;

}

void DlDisplayLoggerReadings(reading_s lreads){

     fprintf(stdout, "Unit: \n");
     fprintf(stdout, "T: %fC     H: %f%     P: %fkPa\n", lreads.temperature, lreads.humidity, lreads.pressure);
     fprintf(stdout, "Xa: %fg     Ya: %fg     Za: %fg\n",lreads.xa,lreads.ya,lreads.za);
     fprintf(stdout, "Pitch: %f     Roll: %f     Yaw: %f\n",lreads.pitch,lreads.roll,lreads.yaw);
     fprintf(stdout, "Xm: %f     Ym: %f     Zm:\n",lreads.xm,lreads.ym,lreads.zm);
     fprintf(stdout, "Latitude: %f    Longitude: %f\n",lreads.latitude,lreads.longitude);
     fprintf(stdout, "Speed: %f     Heading: %f\n\n",lreads.speed,lreads.heading);
}

int DlSaveLoggerData(reading_s creads){

    fprintf(stdout, "Saving Logger Data...\n\n");
    return 0;

}
#endif



