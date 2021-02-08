/** @file vdl.cpp
 *  @author Tsidkeenu Aznar
 *  @date 25JAN2021
 *  @brief Vehicle Data Logger main function
 */
 #include <cstdio>
 #include <unistd.h>
 #include <cinttypes>
 #include <cstring>
 #include <cstdlib>

 #include "vdl.h"
 #include "logger.h"
 #include "logger.cpp"


/** @brief Vehicle Data Logger main function
 *  @author Tsidkeenu Aznar
 *  @date 25JAN2021
 *  @param void
 *  @return int program status
 */
 int main(void)
 {

    while(1)
    {
        fprintf(stdout, "Tsidkeenu Aznar's CENG252 Vehicle Data Logger\n");


        DlInitialization();
        DlGetSerial();
        DlDisplayLoggerReadings(DlGetLoggerReadings());
        DlSaveLoggerData(DlGetLoggerReadings());
        sleep(5);


    }
 }
