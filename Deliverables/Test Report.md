Unit Test Report

|    | Unit action               | Input data or operate                     | Expect result            | Practical result         | Issue | Is it resolved? | How or Why?                                               |
| -- | ------------------------- | ----------------------------------------- | ------------------------ | ------------------------ | ----- | --------------- | --------------------------------------------------------- |
| 1  | Word translation          | Hope真是太聪明了!(select Chinese>>English)| Hope is so clever!       | Hope is so clever!       | NO    | --------------- | --------------------------------------------------------- |
| 2  | Map positioning           | Agree to authorize location information   | Successfully positioned  | Successfully positioned  | NO    | --------------- | --------------------------------------------------------- |
| 3  | Crawling information      | Python Crawling                           | Successfully crawled data| Successfully crawled data| NO    | --------------- | --------------------------------------------------------- |
| 4  | Crawling schedule         | Python Crawling                           | Successfully crawled data| Successfully crawled data| NO    | --------------- | --------------------------------------------------------- |
| 5  | Deploy crawler data       | Deploy to cloud database                  | Successfully crawled data| Successfully deployed    | Yes   | NO              | No method was found for deploying Python code on uniCloud.|
| 6  | Register function         | Username:201918020320 Password:123456     | Successfully registered  | Successfully registered  | No    | --------------- | --------------------------------------------------------- |
| 7  | Login function            | Username:201918020320 Password:123456     | Successfully login       | Successfully login       | No    | --------------- | --------------------------------------------------------- |
| 8  | Set personal information  | Enter all corresponding information       | Successfully set         | Successfully set         | No    | --------------- | --------------------------------------------------------- |
| 9  | Check personal information| Check                                     | Successfully display     | Successfully display     | No    | --------------- | --------------------------------------------------------- |
| 9  | Edit personal information | edit all corresponding information        | Successfully edit        | Successfully edut        | No    | --------------- | --------------------------------------------------------- |
| 10 | Set Grade                 | input SE Level6 Grade:75                  | Successfully set         | Successfully set         | No    | --------------- | --------------------------------------------------------- |
| 11 | Check Grade               | Check                                     | Successfully display     | Successfully display     | No    | --------------- | --------------------------------------------------------- |
| 12 | Edit Grade                | Change SE grade to 80                     | Successfully edit        | Successfully edit        | No    | --------------- | --------------------------------------------------------- |
| 13 | Delete Grade              | Delete Se Grade                           | Successfully delete      | Successfully delete      | No    | --------------- | --------------------------------------------------------- |
| 14 | Set Schedule              | input SPM Maged 6B207 Moday 16:25-18:00   | Successfully set         | Successfully set         | No    | --------------- | --------------------------------------------------------- |
| 15 | Check Schedule            | Check                                     | Successfully display     | Successfully display     | No    | --------------- | --------------------------------------------------------- |
| 16 | Edit Schedule             | Change SPM classroom to 6B307             | Successfully edit        | Successfully edit        | No    | --------------- | --------------------------------------------------------- |
| 17 | Delete Schedule           | Delete SPM Schedule                       | Successfully delete      | Successfully delete      | No    | --------------- | --------------------------------------------------------- |
| 18 | Set Note                  | input 123                                 | Successfully set         | Successfully set         | No    | --------------- | --------------------------------------------------------- |
| 19 | Check Note                | Check                                     | Successfully display     | Successfully display     | No    | --------------- | --------------------------------------------------------- |
| 20 | Edit Note                 | Change 123 to 123456                      | Successfully edit        | Successfully edit        | No    | --------------- | --------------------------------------------------------- |
| 21 | Delete Note               | delete '123456'                           | Successfully delete      | Successfully delete      | No    | --------------- | --------------------------------------------------------- |
| 22 | State management          | click navigator bar wihout login          | Jump to login page       | Jump to login page       | No    | --------------- | --------------------------------------------------------- |


Integration Test Report

|      | Step name                           | Flow Path                                                                                                                                                       |
| ---- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|Step 1| Get an account to login             | open prject >> click User tabbar >> click Regist button >> input correct for account >> Login>>                                                                 |
|Step 2| Operating Personel information      | click Personel information bar >> set information >> edit information>>                                                                                         |
|Step 3| Operating Note                      | click Note tabbar >> click add icon >> input something >> click store note button>> check note >>longpress one note>>click edit >> change something >>          |
|------|-------------------------------------| click edit note >> check note >> longpress one note >> click delete >> check note>>search something >> check note>>                                             |
|Step 4| Operateing Grade                    | click Home tabbar >> click grade navigator bar >> click add icon >> input something >> click store grade button>>check grade>> longpress one note>>click edit >>|
|------|-------------------------------------| change something >> click edit grade >> check grade >> longpress one note >> click delete >> check grade>>search something >> check grade>>                     |
|Step 5| Operateing Schedule                 | click return icon >> click schedule navigator bar >> click add icon >> input something >> click store chedule button>>check schedule>> longpress one note>>     |
|------|-------------------------------------| click edit >>change something >> click edit scheule >> check schedule >> longpress one schedule >> click delete >> check schedule>>                             |
|Step 6| Operateing Map                      | click return icon >> click map navigator bar >> allow geographical location authorization>> check map>>                                                         |
|Step 7|Operateing Translate                 | click return icon >> click translate navigator bar >> input something >> select Chinese to English>> check result>>                                             |
|Step 8|Log out                              | click return icon >> click User tabbar >> click user icon >> select logout                                                                                      |

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
|     | Issue overview                                                                                 | Is it resolved? | How or Why?                               |
| --- | ---------------------------------------------------------------------------------------------- | --------------- | ----------------------------------------- |
|  1  | After adding a note, it was found that system need to log in again                             | Yes             | uni.redirectTo()->uni.switchTab()         |
|  2  | After adding a note/grade/schedule, it was found that page did not refresh to the latest state | Yes             | uni.navigateTo()->uni.redirectTo()        |
|  3  | After search a grade, it was found that page did not refresh to the search page                | Yes             | Calling function name written incorrectly |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#




