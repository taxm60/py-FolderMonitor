using System;
using System.IO;
using System.Threading;

namespace FileMover
{
    class Program
    {
        static void Main(string[] args)
        {
            string username = Environment.UserName;
            string sourceFolder = Path.Combine(@"C:\Users", username, "Downloads");
            string destinationFolder = Path.Combine(sourceFolder, "done");

            Console.WriteLine("------");
            Console.WriteLine("Monitor Folder: " + sourceFolder);
            Console.WriteLine("Target  Folder: " + destinationFolder);
            Console.WriteLine("------");

            while (true)
            {
                MoveCsvFiles(sourceFolder, destinationFolder);
                // Check every 2 seconds (adjust as needed)
                Thread.Sleep(2000);
            }
        }

        static void MoveCsvFiles(string sourceFolder, string destinationFolder)
        {
            // Check if destination folder exists, create if it doesn't
            if (!Directory.Exists(destinationFolder))
            {
                Directory.CreateDirectory(destinationFolder);
            }

            // List all files in the source folder
            string[] files = Directory.GetFiles(sourceFolder);

            foreach (string file in files)
            {
                // Check if file starts with 'f' and ends with '.csv' or '.ods'
                if (Path.GetFileName(file).StartsWith("f") &&
                    (Path.GetExtension(file).Equals(".csv", StringComparison.OrdinalIgnoreCase) ||
                     Path.GetExtension(file).Equals(".ods", StringComparison.OrdinalIgnoreCase)))
                {
                    // Construct full paths for source and destination
                    string destinationFile = Path.Combine(destinationFolder, Path.GetFileName(file));

                    // Check if the destination file exists, delete it if necessary
                    if (File.Exists(destinationFile))
                    {
                        File.Delete(destinationFile);
                    }

                    // Move the file to the destination folder
                    try
                    {
                        File.Copy(file, destinationFile);
                        File.Delete(file);  // Optionally delete the original file after successful copy
                        Console.WriteLine($"[O] Moving: {file} -> {destinationFile}");
                    }
                    catch (IOException e)
                    {
                        Console.WriteLine($"[X] IO Error: {e.Message}");
                    }
                    catch (UnauthorizedAccessException e)
                    {
                        Console.WriteLine($"[X] Unauthorized Access: {e.Message}");
                    }
                    catch (Exception e)
                    {
                        Console.WriteLine($"[X] Unexpected error: {e.Message}");
                    }
                }
            }
        }
    }
}
