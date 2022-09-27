#ADF file loader
#contains 1 class, ADF_loader, which accepts the path of the file to be opened as its argument


import struct


class ADF_loader:
    def __init__(self,filename):
        
        self.fh = open(filename, mode= 'rb')#, encoding='cp037')
        self.fid = self.fh.read(512)
        
        self.framesLeft,self.i=self.fread(self.fid ,0,1,'int16')           # number of image planes remaining, inclusive [0]
        self.width,self.i=self.fread(self.fid, 2,1,'int16')              # frame width (pixels) [2] 
        self.height,self.i=self.fread(self.fid, 4,1,'int16')             #% frame height (pixels) [4]
        self.bytesPerPixel,self.i=self.fread(self.fid, 6 ,1,'int16')       # % bytes per pixel [6]
        self.bitsPerPixel,self.i=self.fread(self.fid,8,1,'int16')#         % bits per pixel [8]
        self.year,self.i=self.fread(self.fid,10,1,'int16')#              % Computer local year [10]
        self.day,self.i=self.fread(self.fid,12,1,'int16')#              % Computer local days from beginning of year [12]
        self.hour,self.i=self.fread(self.fid,14,1,'int16')#              % Computer local hour [14]
        self.minute,self.i=self.fread(self.fid,16,1,'int16')#              % minute [16]
        self.sec,self.i=self.fread(self.fid,18,1,'int16')#                 % second [18]
        self.msec,self.i=self.fread(self.fid,20,1,'int16')#;				  % millisecond [20]
        self.frameRate,self.i=self.fread(self.fid,22,1,'int16')#;            % frame rate (Hz) [22]
        self.intTime,self.i=self.fread(self.fid,24,1,'uint32')#;            % integration time (msec) [24]
        self.seekerFrameNumber,self.i=self.fread(self.fid,28,1,'uint32')#;	  % Seeker frame number... [28]
        self.sensorElevationAng,self.i=self.fread(self.fid,32,1,'float32')#; % Sensor elevation in degrees[32]
        self.sensorAzimuthAng,self.i=self.fread(self.fid,36,1,'float32')#;	  % Sensor azimuth in degrees[36]
        self.sensorRoll,self.i=self.fread(self.fid,40,1,'float32')#;	      % Sensor roll in degrees[40]
        self.Hifov,self.i=self.fread(self.fid,44,1,'float32')#;			  % horizontal ifov (mrad) [44]
        self.Vifov,self.i=self.fread(self.fid,48,1,'float32')#;			  % vertical ifov (mrad) [48]
        self.FiltCuton,self.i=self.fread(self.fid,52,1,'float32')#;		  % filter cut-on wavelength (microns) [52]
        self.FiltCutoff,self.i=self.fread(self.fid,56,1,'float32')#;		  % filter cut-off wavelength (microns) [56]
        self.MaxTrans,self.i=self.fread(self.fid,60,1,'float32')#; 		  % max transmittance (%) [60]
        self.slantRange,self.i=self.fread(self.fid,64,1,'float32')#;            % target slant range (m) [64]
        self.tgtAspect,self.i=self.fread(self.fid,68,1,'float32')#;		  % target aspect (deg - 0 front, 90 right) [68]
        self.tgtElevation,self.i=self.fread(self.fid,72,1,'float32')#;		  % target elevation (deg - 0 level, 90 top) [72]
        self.rAtmTemp,self.i=self.fread(self.fid,76,1,'float32')#; 		  % atmospheric temp (K) [76]
        self.dewPoint,self.i=self.fread(self.fid,80,1,'float32')#; 		  % dewpoint temp (K) [80]
        self.visibility,self.i=self.fread(self.fid,84,1,'float32')#;		  % atmospheric visibility (km) [84]
        self.relHumidity,self.i=self.fread(self.fid,88,1,'float32')#;	      % atmospheric relative humidity (%) [88]
        self.atmTrans,self.i=self.fread(self.fid,92,1,'float32')#; 		  % atmospheric transmittance (%) [92]
        self.atmPressure,self.i=self.fread(self.fid,96,1,'float32')#;	      % atmospheric pressure (mbar) [96]
        self.RefTemp,self.i=self.fread(self.fid,100,1,'float32')#;  		  % reflected ambient temp (K) [100]
        self.NUCHigh,self.i=self.fread(self.fid,104,1,'float32')#;  		  % N.U.C. source high temp (K) [104]
        self.NUCLow,self.i=self.fread(self.fid,108,1,'float32')#;			  % N.U.C. source low temp (K) [108]
        self.hszCamera,self.i=self.fread(self.fid,112,16,'uint8')#;		      % camera type, serial number, etc. (16 bytes) [112]

        self.estMslPosX,self.i=self.fread(self.fid,128,1,'float32')#;         %Estimate Msl Position[128]
        self.estMslPosY,self.i=self.fread(self.fid,132,1,'float32')#;
        self.estMslPosZ,self.i=self.fread(self.fid,136,1,'float32')#;
        self.estMslVelX,self.i=self.fread(self.fid,140,1,'float32')#;         %Esitmate Msl Vel[140]
        self.estMslVelY,self.i=self.fread(self.fid,144,1,'float32')#;
        self.estMslVelZ,self.i=self.fread(self.fid,148,1,'float32')#;
        self.estMslYaw,self.i=self.fread(self.fid,152,1,'float32')#;          %Estimated Euler Angles[152]
        self.estMslPitch,self.i=self.fread(self.fid,156,1,'float32')#;
        self.estMslRoll,self.i=self.fread(self.fid,160,1,'float32')#;
        self.targetBoxX0,self.i=self.fread(self.fid,164,1,'int16')#;        % [164] pixel location in az of target designation box as measured from top left corner of upright image
        self.targetBoxY0,self.i=self.fread(self.fid,166,1,'int16')#;        %  [166] pixel location in el of target designation box as measured from top left corner of upright image
        self.targetBoxX1,self.i=self.fread(self.fid,168,1,'int16')#;        %  [168] pixel location in az of target designation box as measured from top left corner of upright image
        self.targetBoxY1,self.i=self.fread(self.fid,170,1,'int16')#;        %  [170] pixel location in el of target designation box as measured from top left corner of upright image
        self.targetBoxX2,self.i=self.fread(self.fid,172,1,'int16')#;        %  [172] pixel location in az of target designation box as measured from top left corner of upright image
        self.targetBoxY2,self.i=self.fread(self.fid,174,1,'int16')#;        %  [174] pixel location in el of target designation box as measured from top left corner of upright image
        self.targetBoxX3,self.i=self.fread(self.fid,176,1,'int16')#;        %  [176] pixel location in az of target designation box as measured from top left corner of upright image
        self.targetBoxY3,self.i=self.fread(self.fid,178,1,'int16')#;       %  [178] pixel location in el of target designation box as measured from top left corner of upright image
        self.targetBoxX4,self.i=self.fread(self.fid,180,1,'int16')#;        %  [180] pixel location in az of target designation box as measured from top left corner of upright image
        self.targetBoxY4,self.i=self.fread(self.fid,182,1,'int16')#;        %  [182] pixel location in el of target designation box as measured from top left corner of upright image
        self.targetBoxX5,self.i=self.fread(self.fid,184,1,'int16')#;        %  [184] pixel location in az of target designation box as measured from top left corner of upright image
        self.targetBoxY5,self.i=self.fread(self.fid,186,1,'int16')#;        %  [186] pixel location in el of target designation box as measured from top left corner of upright image
        self.targetBoxX6,self.i=self.fread(self.fid,188,1,'int16')#;        %  [188] pixel location in az of target designation box as measured from top left corner of upright image
        self.targetBoxY6,self.i=self.fread(self.fid,190,1,'int16')#;        %  [190] pixel location in el of target designation box as measured from top left corner of upright image
        self.targetBoxX7,self.i=self.fread(self.fid,192,1,'int16')#;        %  [192] pixel location in az of target designation box as measured from top left corner of upright image
        self.targetBoxY7,self.i=self.fread(self.fid,194,1,'int16')#;        %  [194] pixel location in az of target designation box as measured from top left corner of upright image

        self.truMslPosX,self.i=self.fread(self.fid,196,1,'float32')#;         %true Msl Position[196]
        self.truMslPosY,self.i=self.fread(self.fid,200,1,'float32')#;
        self.truMslPosZ,self.i=self.fread(self.fid,204,1,'float32')#;
        self.truMslVelX,self.i=self.fread(self.fid,208,1,'float32')#;         %true Msl Vel[208]
        self.truMslVelY,self.i=self.fread(self.fid,212,1,'float32')#;
        self.truMslVelZ,self.i=self.fread(self.fid,216,1,'float32')#;
        self.truMslYaw,self.i=self.fread(self.fid,220,1,'float32')#           %true Euler Angles[220]
        self.truMslPitch,self.i=self.fread(self.fid,224,1,'float32')#;
        self.truMslRoll,self.i=self.fread(self.fid,228,1,'float32')#;

        self.estTgtPosX,self.i=self.fread(self.fid,232,1,'float32')#;         %Estimated Tgt Position[232]
        self.estTgtPosY,self.i=self.fread(self.fid,236,1,'float32')#;
        self.estTgtPosZ,self.i=self.fread(self.fid,240,1,'float32')#;
        self.truTgtPosX,self.i=self.fread(self.fid,244,1,'float32')#;         %true Tgt Position[244]
        self.truTgtPosY,self.i=self.fread(self.fid,248,1,'float32')#;
        self.truTgtPosZ,self.i=self.fread(self.fid,252,1,'float32')#;

        self.numberOfChannels,self.i=self.fread(self.fid,256,1,'uint8')#;     % [256]
        self.channelFormat,self.i=self.fread(self.fid,257,1,'uint8')#;        % [257]
        self.hszTgt,self.i=self.fread(self.fid,258,16,'uint8')#;			  % target type (16 bytes) [258]
        self.hszEngType,self.i=self.fread(self.fid,274,16,'uint8')#; 	      % engine type (16 bytes) [274]
        self.hszEngState,self.i=self.fread(self.fid,290,16,'uint8')#;         % engine state (16 bytes) [290]
        self.calOffset,self.i=self.fread(self.fid,306,1,'float32')#;		  % calibration offset (mW/sr) [306]
        self.calSlope,self.i=self.fread(self.fid,310,1,'float32')#; 		  % calibration slope (microW/sr) [310]
        self.month,self.i=self.fread(self.fid,314,1,'uint8')#;				  % Month in the year (Jan:0, Feb:1, Mar:2, ... Dec:11) [314]
        self.dayOfMonth,self.i=self.fread(self.fid,315,1,'uint8')#;			  % Day of the month (byte) [315]

        #GPS Position from RMC message
        self.gpsValid,self.i=self.fread(self.fid,316,1,'uint8')#; 		      % GPS Valid (0 or 1) [316]
        self.gpsFixQuality,self.i=self.fread(self.fid,317,1,'uint8')#; 		  % GPS Fix Quality (0 or 1) [317]

        self.latDeg,self.i=self.fread(self.fid,318,1,'int16')#;				  % Latitude Degrees (+ = North, - = South) [318]
        self.latMinute,self.i=self.fread(self.fid,320,1,'int16')#;		      % Latitude Minutes [320]
        self.latMinFract,self.i=self.fread(self.fid,322,1,'int16')#;		  % Latitude Minute Fraction (0.001 Minutes) [322]
        self.longDeg,self.i=self.fread(self.fid,324,1,'int16')#;  		      % Longitude Degrees (+ = West, - = East) [324]
        self.longMinute,self.i=self.fread(self.fid,326,1,'int16')#;			  % Longitude Minutes [326]
        self.longMinFract,self.i=self.fread(self.fid,328,1,'int16')#;		  % Longitude Minute Fraction (0.001 Minutes) [328]
        self.courseHeading,self.i=self.fread(self.fid,330,1,'float32')#;	  % True Course Heading (0.1 degrees) [330]
        self.groundSpeed,self.i=self.fread(self.fid,334,1,'float32')#;		  % Ground speed (0.1 Knots) [334]
        self.magneticVar,self.i=self.fread(self.fid,338,1,'float32')#;		  % Magnetic Variation (0.1 degrees, + = West) [338]

        # GPS Time and Date...
        self.gpsHour,self.i=self.fread(self.fid,342,1,'int16')#;  		      % GPS Hour [342]
        self.gpsMinute,self.i=self.fread(self.fid,344,1,'int16')#;            % GPS Minute [344]
        self.gpsSecond,self.i=self.fread(self.fid,346,1,'int16')#;            % GPS Second [346]
        self.gpsYear,self.i=self.fread(self.fid,348,1,'int16')#;              % GPS Year (97 98 99 00 01 ...) [348]
        self.gpsMonth,self.i=self.fread(self.fid,350,1,'int16')#;             % GPS Month (1 - Jan, 2 - Feb, ...) [350]
        self.gpsDay,self.i=self.fread(self.fid,352,1,'int16')#;	              % GPS Day of Month [352]

        # GPS Info from GGA message
        self.antHeight,self.i=self.fread(self.fid,254,1,'float32')#;          % Height of GPS antenna above/below mean sea level (0.1 m) [354]
        self.geodHeight,self.i=self.fread(self.fid,258,1,'float32')#;		  % Geoidal height (0.1 m) [358]
        self.numSat,self.i=self.fread(self.fid,262,1,'int16')#;				  % Number of Satillites acquired [362]
        self.horizPrecision,self.i=self.fread(self.fid,364,1,'float32')#;	  % Horizontal dilution of precision (0.1 %) [364]

        self.pad2,self.i=self.fread(self.fid,368,6,'uint8')#;                  % 6 byte pad [368]

        # Color Camera info
        self.rowStart,self.i=self.fread(self.fid,374,1,'int16')#; 		      % first row being grabbed [374]
        self.colStart,self.i=self.fread(self.fid,376,1,'int16')#; 		      % first column being grabbed [376]
        self.green1Gain,self.i=self.fread(self.fid,378,1,'int16')#;			  % gain for green 1 pixels [378]
        self.blueGain,self.i=self.fread(self.fid,380,1,'int16')#; 		      % gain for blue pixels [380]
        self.redGain,self.i=self.fread(self.fid,382,1,'int16')#;  		      % gain for red pixels [382]
        self.green2Gain,self.i=self.fread(self.fid,384,1,'int16')#;			  % gain for green 2 pixels [384]
        self.green1Offset,self.i=self.fread(self.fid,386,1,'int16')#;		  % offset for green 1 pixels [386]
        self.green2Offset,self.i=self.fread(self.fid,388,1,'int16')#;		  % offset for green 2 pixels [388]
        self.redOffset,self.i=self.fread(self.fid,390,1,'int16')#;		      % offset for red pixels [390]
        self.blueOffset,self.i=self.fread(self.fid,392,1,'int16')#;			  % offset for blue pixels [392]
        self.blackLevel,self.i=self.fread(self.fid,394,1,'int16')#;			  % black level [394]
        self.horizBlank,self.i=self.fread(self.fid,396,1,'int16')#;			  % horizontal blanking [396]

        self.masterTime,self.i=self.fread(self.fid,398,1,'double')#;	      % Seconds since Jan 1, 1970... [398]

        self.platformTOV,self.i=self.fread(self.fid,406,1,'double')#;         % Time of validity, UTC elapsed seconds (NEED TO DEFINE THIS)  [406]
        self.platformHeading,self.i=self.fread(self.fid,414,1,'float32')#;    % Platform Heading in degrees (0 - 359.99 deg)  [414]
        self.platformPitch,self.i=self.fread(self.fid,418,1,'float32')#;      % Platform Pitch in degrees (+/- 180 deg)  [418]
        self.platformRoll,self.i=self.fread(self.fid,422,1,'float32')#;       % Platform Roll in degrees  (+/- 180 deg)  [422]
        self.platformAltitude,self.i=self.fread(self.fid,426,1,'float32')#;   % Platform latitude in degrees  (+/- 90 deg)  [426]
        self.platformLatitude,self.i=self.fread(self.fid,430,1,'float32')#;   % Platform longitude in degrees (+/- 90 deg)  [430]
        self.platformLongitude,self.i=self.fread(self.fid,434,1,'float32')#;  % Platform altitude meters above sea level  [434]
        self.targetID,self.i=self.fread(self.fid,438,1,'int16')#;             % LOCAITS target ID  [438]
        self.rgetTime,self.i=self.fread(self.fid,440,1,'float32')#;           % LOCAITS message time  [440]
        self.targetLatitude,self.i=self.fread(self.fid,444,1,'float32')#;     % LOCAITS target latitude in degrees  (+/-  90.0 deg)  [444]
        self.targetLongitude,self.i=self.fread(self.fid,448,1,'float32')#;    % LOCAITS target longitude in degrees (+/- 180.0 deg)  [448]
        self.targetAltitude,self.i=self.fread(self.fid,452,1,'float32')#;     % LOCAITS target altitude in meters above sea level  [452]

        self.hszComment,self.i=self.fread(self.fid,456,44,'uint8')#;          % comment (51 bytes) [457]

        self.targetSpeed,self.i=self.fread(self.fid,500,1,'float32')#;
        self.targetDirection,self.i=self.fread(self.fid,504,1,'float32')#;
        self.majorVersion,self.i=self.fread(self.fid,508,1,'uint8')#;         % Major Version for this header is 2 [508]
        self.minorVersion,self.i=self.fread(self.fid,509,1,'uint8')#;         % Minor Version for this header is 3 [509]
        self.sizeOfSecondHeader,self.i=self.fread(self.fid,510,1,'int16')#;   % Size of a second header that would folow this one ...  [510]


        self.frameTime=self.hour*3600.0 + 60.0*self.minute + 1.0*self.sec + 0.001*self.msec#;
    
    
    def fread(self,header, start, nbytes, precision ):    
        if (precision == 'uint8'):
            self.size = nbytes
            self.data = int.from_bytes(header[start: start+self.size], byteorder="little")
        if (precision == 'int16'):
            self.size = nbytes *2
            self.data = int.from_bytes(header[start: start+self.size], byteorder="little")
        if (precision == 'uint32'):
            self.size = nbytes *4
            self.data = int.from_bytes(header[start: start+self.size], byteorder="little")
        if (precision == "float32"):
            self.size = nbytes * 4 
            self.data = struct.unpack('<f',header[start: start+self.size])
        if (precision == "double"):
            self.size = nbytes * 8 
            data = struct.unpack('d',header[start: start+self.size])
        return self.data , start+self.size







