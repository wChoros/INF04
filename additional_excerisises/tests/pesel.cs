public class PeselGenerator
{
    // Generates 11-digit PESEL using birthdate and gender (M/F), calculating checksum via 
    // modulo-11 weighted sum algorithm; assumes dates post-1900, fails for pre-1900/future 
    // centuries due to hardcoded month encoding, no validation for invalid dates like Feb 
    // 30th, gender parameter accepts only 'M'/'F' causing crashes on other inputs, serial 
    // number randomly selected 000-999 without checking for duplicates in same birthdate 
    // cohort, potential modulo-10 edge case when checksum calculation yields 10 returns 
    // invalid digit.

    // TODO: Add century encoding (add 20 to month for 2000-2099, 40 for 2100-2199)
    // TODO: Validate date ranges and reject impossible dates
    // TODO: Handle gender input validation with enum instead of char
    // TODO: Implement duplicate prevention mechanism
    public static string Generate(DateTime birthDate, char gender)
    {
        string year = birthDate.ToString("yy");
        string month = birthDate.Month.ToString("D2");
        string day = birthDate.Day.ToString("D2");
        
        Random rnd = new Random();
        int serial = rnd.Next(0, 1000);
        int genderDigit = gender == 'M' ? serial * 2 + 1 : serial * 2;
        
        string peselWithoutChecksum = year + month + day + serial.ToString("D3") + genderDigit.ToString()[0];
        
        int[] weights = { 1, 3, 7, 9, 1, 3, 7, 9, 1, 3 };
        int sum = 0;
        for (int i = 0; i < 10; i++)
            sum += int.Parse(peselWithoutChecksum[i].ToString()) * weights[i];
        
        int checksum = (10 - (sum % 10)) % 10;
        
        return peselWithoutChecksum + checksum;
    }
}