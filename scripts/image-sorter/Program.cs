﻿using ExifLibrary;
using System;
using System.Text;
using System.Text.RegularExpressions;

namespace ImageSort
{
    internal class Program
    {
        static DateTime blankDateTime = new DateTime(0);

        static void Main(string[] args)
        {
            // change this path
            string path = @"/home/freeman/Pictures/DCIM";
            string[] files = Directory.GetFiles(path);

            int i = 0;
            foreach (string file in files)
            {
                DateTime dateTime = GetImageYear(file);
    


                string fileName = Path.GetFileName(file);

                // if no date is saved, try to extract it from the filename
                if (dateTime == blankDateTime)
                {
                    dateTime = ExtractDateFromFileName(fileName);
                }
                

                if (dateTime == blankDateTime)
                {
                    // do nothing
                    string[] dirPaths = {path,"nodate"};
                    CreateDirIfNotExists(Path.Combine(dirPaths));
                    
                    string[] filePaths = {path,"nodate",fileName};
                    string newFilePath = Path.Combine(filePaths);
                    File.Copy(file, newFilePath);
                }
                else
                {
                    string[] dirPaths = {path,dateTime.Year.ToString()};
                    CreateDirIfNotExists(Path.Combine(dirPaths));

                    string[] filePaths = {path,dateTime.Year.ToString(),fileName};
                    string newFilePath = Path.Combine(filePaths);
                    File.Copy(file, newFilePath);

                    File.SetCreationTime(newFilePath, dateTime);
                    File.SetLastAccessTime(newFilePath, dateTime);
                    File.SetLastWriteTime(newFilePath, dateTime);
                }

                i++;
                Console.WriteLine(i + "/" + files.Length);
                
            }
            
            
        }

        public static void CreateDirIfNotExists(string path)
        {
            if (!Directory.Exists(path))
            {
                Directory.CreateDirectory(path);
            }
        }
        
        static DateTime ExtractDateFromFileName(string fileName)
        {
            // Define the pattern for the specified format
            string pattern = @"^IMG-(\d{8})-WA\d{4}\.jpg$";

            // Check if the file name matches the pattern
            Match match = Regex.Match(fileName, pattern);

            // If there is a match, extract the date from the matched group
            if (match.Success)
            {
                string dateString = match.Groups[1].Value;

                // Parse the extracted date string into a DateTime object
                if (DateTime.TryParseExact(dateString, "yyyyMMdd", null, System.Globalization.DateTimeStyles.None, out DateTime result))
                {
                    return result;
                }
            }
            
            
            // VID match
            string patternVideo = @"^VID-(\d{8})-WA\d{4}\.mp4$";

            // Check if the file name matches the pattern
            Match matchV = Regex.Match(fileName, patternVideo);

            // If there is a match, extract the date from the matched group
            if (matchV.Success)
            {
                string dateString = matchV.Groups[1].Value;

                // Parse the extracted date string into a DateTime object
                if (DateTime.TryParseExact(dateString, "yyyyMMdd", null, System.Globalization.DateTimeStyles.None, out DateTime result))
                {
                    return result;
                }
            }
            
            //PXL match
            string patternP = @"^PXL_(\d{8})_(\d{9})\.(jpg|mp4)$";

            // Check if the file name matches the pattern
            Match matchP = Regex.Match(fileName, patternP);

            // If there is a match, extract the date from the matched groups
            if (matchP.Success)
            {
                string dateString = matchP.Groups[1].Value;
                string timeString = matchP.Groups[2].Value;

                // Combine date and time parts and parse into a DateTime object
                string dateTimeString = dateString + timeString;
                if (DateTime.TryParseExact(dateTimeString, "yyyyMMddHHmmssfff", null, System.Globalization.DateTimeStyles.None, out DateTime result))
                {
                    return result;
                }
            }
            
            // VID2 match
            string patternV2 = @"^VID(\d{14})\.mp4$";

            // Check if the file name matches the pattern
            Match matchV2 = Regex.Match(fileName, patternV2);

            // If there is a match, extract the date from the matched group
            if (matchV2.Success)
            {
                string dateString = matchV2.Groups[1].Value;

                // Parse the extracted date string into a DateTime object
                if (DateTime.TryParseExact(dateString, "yyyyMMddHHmmss", null, System.Globalization.DateTimeStyles.None, out DateTime result))
                {
                    return result;
                }
            }
            
            // Snapchat match
            // Define the pattern for the specified formats with mp4 or jpg extension
            string patternSnap = @"^Snapchat-(\d{8})\.(\d{6})\d{2}\.(mp4|jpg)$";

            // Check if the file name matches the pattern
            Match matchSnap = Regex.Match(fileName, patternSnap);

            // If there is a match, extract the date from the matched groups
            if (matchSnap.Success)
            {
                string dateString = matchSnap.Groups[1].Value;
                string timeString = matchSnap.Groups[2].Value;

                // Combine date and time parts and parse into a DateTime object
                string dateTimeString = dateString + timeString;
                if (DateTime.TryParseExact(dateTimeString, "yyyyMMddHHmmss", null, System.Globalization.DateTimeStyles.None, out DateTime result))
                {
                    return result;
                }
            }
            
            

            // Return null if the file name does not match the specified format or if parsing fails
            return blankDateTime;
        }

        public static DateTime GetImageYear(string imagePath)
        {

            var blank = new DateTime(0);

            try
            {

                var file = ImageFile.FromFile(imagePath);
                foreach (var property in file.Properties)
                {
                    //Console.WriteLine(property.Name);
                    if (property.Name == "DateTime")
                    {
                        return file.Properties.Get<ExifDateTime>(ExifTag.DateTime);
                    }
                }

                return blankDateTime;
            }
            catch (Exception)
            {
                return blankDateTime;
            }
        }
    }
}
