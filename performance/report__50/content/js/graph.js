/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
$(document).ready(function() {

    $(".click-title").mouseenter( function(    e){
        e.preventDefault();
        this.style.cursor="pointer";
    });
    $(".click-title").mousedown( function(event){
        event.preventDefault();
    });

    // Ugly code while this script is shared among several pages
    try{
        refreshHitsPerSecond(true);
    } catch(e){}
    try{
        refreshResponseTimeOverTime(true);
    } catch(e){}
    try{
        refreshResponseTimePercentiles();
    } catch(e){}
});


var responseTimePercentilesInfos = {
        data: {"result": {"minY": 61.0, "minX": 0.0, "maxY": 5023.0, "series": [{"data": [[0.0, 61.0], [0.1, 73.0], [0.2, 76.0], [0.3, 77.0], [0.4, 78.0], [0.5, 79.0], [0.6, 80.0], [0.7, 81.0], [0.8, 81.0], [0.9, 82.0], [1.0, 82.0], [1.1, 83.0], [1.2, 83.0], [1.3, 84.0], [1.4, 84.0], [1.5, 84.0], [1.6, 85.0], [1.7, 85.0], [1.8, 86.0], [1.9, 86.0], [2.0, 86.0], [2.1, 87.0], [2.2, 87.0], [2.3, 87.0], [2.4, 87.0], [2.5, 88.0], [2.6, 88.0], [2.7, 88.0], [2.8, 88.0], [2.9, 89.0], [3.0, 89.0], [3.1, 89.0], [3.2, 89.0], [3.3, 90.0], [3.4, 90.0], [3.5, 90.0], [3.6, 90.0], [3.7, 91.0], [3.8, 91.0], [3.9, 91.0], [4.0, 91.0], [4.1, 91.0], [4.2, 92.0], [4.3, 92.0], [4.4, 92.0], [4.5, 92.0], [4.6, 92.0], [4.7, 93.0], [4.8, 93.0], [4.9, 93.0], [5.0, 93.0], [5.1, 93.0], [5.2, 93.0], [5.3, 94.0], [5.4, 94.0], [5.5, 94.0], [5.6, 94.0], [5.7, 94.0], [5.8, 94.0], [5.9, 95.0], [6.0, 95.0], [6.1, 95.0], [6.2, 95.0], [6.3, 95.0], [6.4, 95.0], [6.5, 96.0], [6.6, 96.0], [6.7, 96.0], [6.8, 96.0], [6.9, 96.0], [7.0, 96.0], [7.1, 96.0], [7.2, 97.0], [7.3, 97.0], [7.4, 97.0], [7.5, 97.0], [7.6, 97.0], [7.7, 97.0], [7.8, 97.0], [7.9, 98.0], [8.0, 98.0], [8.1, 98.0], [8.2, 98.0], [8.3, 98.0], [8.4, 98.0], [8.5, 98.0], [8.6, 98.0], [8.7, 99.0], [8.8, 99.0], [8.9, 99.0], [9.0, 99.0], [9.1, 99.0], [9.2, 99.0], [9.3, 99.0], [9.4, 99.0], [9.5, 100.0], [9.6, 100.0], [9.7, 100.0], [9.8, 100.0], [9.9, 100.0], [10.0, 100.0], [10.1, 100.0], [10.2, 100.0], [10.3, 101.0], [10.4, 101.0], [10.5, 101.0], [10.6, 101.0], [10.7, 101.0], [10.8, 101.0], [10.9, 101.0], [11.0, 101.0], [11.1, 101.0], [11.2, 101.0], [11.3, 102.0], [11.4, 102.0], [11.5, 102.0], [11.6, 102.0], [11.7, 102.0], [11.8, 102.0], [11.9, 102.0], [12.0, 102.0], [12.1, 102.0], [12.2, 103.0], [12.3, 103.0], [12.4, 103.0], [12.5, 103.0], [12.6, 103.0], [12.7, 103.0], [12.8, 103.0], [12.9, 103.0], [13.0, 103.0], [13.1, 103.0], [13.2, 104.0], [13.3, 104.0], [13.4, 104.0], [13.5, 104.0], [13.6, 104.0], [13.7, 104.0], [13.8, 104.0], [13.9, 104.0], [14.0, 104.0], [14.1, 104.0], [14.2, 105.0], [14.3, 105.0], [14.4, 105.0], [14.5, 105.0], [14.6, 105.0], [14.7, 105.0], [14.8, 105.0], [14.9, 105.0], [15.0, 105.0], [15.1, 105.0], [15.2, 106.0], [15.3, 106.0], [15.4, 106.0], [15.5, 106.0], [15.6, 106.0], [15.7, 106.0], [15.8, 106.0], [15.9, 106.0], [16.0, 106.0], [16.1, 106.0], [16.2, 106.0], [16.3, 107.0], [16.4, 107.0], [16.5, 107.0], [16.6, 107.0], [16.7, 107.0], [16.8, 107.0], [16.9, 107.0], [17.0, 107.0], [17.1, 107.0], [17.2, 107.0], [17.3, 107.0], [17.4, 108.0], [17.5, 108.0], [17.6, 108.0], [17.7, 108.0], [17.8, 108.0], [17.9, 108.0], [18.0, 108.0], [18.1, 108.0], [18.2, 108.0], [18.3, 108.0], [18.4, 108.0], [18.5, 109.0], [18.6, 109.0], [18.7, 109.0], [18.8, 109.0], [18.9, 109.0], [19.0, 109.0], [19.1, 109.0], [19.2, 109.0], [19.3, 109.0], [19.4, 109.0], [19.5, 109.0], [19.6, 110.0], [19.7, 110.0], [19.8, 110.0], [19.9, 110.0], [20.0, 110.0], [20.1, 110.0], [20.2, 110.0], [20.3, 110.0], [20.4, 110.0], [20.5, 110.0], [20.6, 110.0], [20.7, 110.0], [20.8, 111.0], [20.9, 111.0], [21.0, 111.0], [21.1, 111.0], [21.2, 111.0], [21.3, 111.0], [21.4, 111.0], [21.5, 111.0], [21.6, 111.0], [21.7, 111.0], [21.8, 111.0], [21.9, 111.0], [22.0, 112.0], [22.1, 112.0], [22.2, 112.0], [22.3, 112.0], [22.4, 112.0], [22.5, 112.0], [22.6, 112.0], [22.7, 112.0], [22.8, 112.0], [22.9, 112.0], [23.0, 112.0], [23.1, 112.0], [23.2, 112.0], [23.3, 113.0], [23.4, 113.0], [23.5, 113.0], [23.6, 113.0], [23.7, 113.0], [23.8, 113.0], [23.9, 113.0], [24.0, 113.0], [24.1, 113.0], [24.2, 113.0], [24.3, 113.0], [24.4, 113.0], [24.5, 114.0], [24.6, 114.0], [24.7, 114.0], [24.8, 114.0], [24.9, 114.0], [25.0, 114.0], [25.1, 114.0], [25.2, 114.0], [25.3, 114.0], [25.4, 114.0], [25.5, 114.0], [25.6, 114.0], [25.7, 114.0], [25.8, 115.0], [25.9, 115.0], [26.0, 115.0], [26.1, 115.0], [26.2, 115.0], [26.3, 115.0], [26.4, 115.0], [26.5, 115.0], [26.6, 115.0], [26.7, 115.0], [26.8, 115.0], [26.9, 115.0], [27.0, 115.0], [27.1, 116.0], [27.2, 116.0], [27.3, 116.0], [27.4, 116.0], [27.5, 116.0], [27.6, 116.0], [27.7, 116.0], [27.8, 116.0], [27.9, 116.0], [28.0, 116.0], [28.1, 116.0], [28.2, 116.0], [28.3, 116.0], [28.4, 117.0], [28.5, 117.0], [28.6, 117.0], [28.7, 117.0], [28.8, 117.0], [28.9, 117.0], [29.0, 117.0], [29.1, 117.0], [29.2, 117.0], [29.3, 117.0], [29.4, 117.0], [29.5, 117.0], [29.6, 117.0], [29.7, 118.0], [29.8, 118.0], [29.9, 118.0], [30.0, 118.0], [30.1, 118.0], [30.2, 118.0], [30.3, 118.0], [30.4, 118.0], [30.5, 118.0], [30.6, 118.0], [30.7, 118.0], [30.8, 118.0], [30.9, 119.0], [31.0, 119.0], [31.1, 119.0], [31.2, 119.0], [31.3, 119.0], [31.4, 119.0], [31.5, 119.0], [31.6, 119.0], [31.7, 119.0], [31.8, 119.0], [31.9, 119.0], [32.0, 119.0], [32.1, 119.0], [32.2, 120.0], [32.3, 120.0], [32.4, 120.0], [32.5, 120.0], [32.6, 120.0], [32.7, 120.0], [32.8, 120.0], [32.9, 120.0], [33.0, 120.0], [33.1, 120.0], [33.2, 120.0], [33.3, 120.0], [33.4, 120.0], [33.5, 121.0], [33.6, 121.0], [33.7, 121.0], [33.8, 121.0], [33.9, 121.0], [34.0, 121.0], [34.1, 121.0], [34.2, 121.0], [34.3, 121.0], [34.4, 121.0], [34.5, 121.0], [34.6, 121.0], [34.7, 121.0], [34.8, 122.0], [34.9, 122.0], [35.0, 122.0], [35.1, 122.0], [35.2, 122.0], [35.3, 122.0], [35.4, 122.0], [35.5, 122.0], [35.6, 122.0], [35.7, 122.0], [35.8, 122.0], [35.9, 122.0], [36.0, 122.0], [36.1, 123.0], [36.2, 123.0], [36.3, 123.0], [36.4, 123.0], [36.5, 123.0], [36.6, 123.0], [36.7, 123.0], [36.8, 123.0], [36.9, 123.0], [37.0, 123.0], [37.1, 123.0], [37.2, 123.0], [37.3, 124.0], [37.4, 124.0], [37.5, 124.0], [37.6, 124.0], [37.7, 124.0], [37.8, 124.0], [37.9, 124.0], [38.0, 124.0], [38.1, 124.0], [38.2, 124.0], [38.3, 124.0], [38.4, 124.0], [38.5, 124.0], [38.6, 125.0], [38.7, 125.0], [38.8, 125.0], [38.9, 125.0], [39.0, 125.0], [39.1, 125.0], [39.2, 125.0], [39.3, 125.0], [39.4, 125.0], [39.5, 125.0], [39.6, 125.0], [39.7, 125.0], [39.8, 126.0], [39.9, 126.0], [40.0, 126.0], [40.1, 126.0], [40.2, 126.0], [40.3, 126.0], [40.4, 126.0], [40.5, 126.0], [40.6, 126.0], [40.7, 126.0], [40.8, 126.0], [40.9, 127.0], [41.0, 127.0], [41.1, 127.0], [41.2, 127.0], [41.3, 127.0], [41.4, 127.0], [41.5, 127.0], [41.6, 127.0], [41.7, 127.0], [41.8, 127.0], [41.9, 127.0], [42.0, 127.0], [42.1, 128.0], [42.2, 128.0], [42.3, 128.0], [42.4, 128.0], [42.5, 128.0], [42.6, 128.0], [42.7, 128.0], [42.8, 128.0], [42.9, 128.0], [43.0, 128.0], [43.1, 128.0], [43.2, 129.0], [43.3, 129.0], [43.4, 129.0], [43.5, 129.0], [43.6, 129.0], [43.7, 129.0], [43.8, 129.0], [43.9, 129.0], [44.0, 129.0], [44.1, 129.0], [44.2, 129.0], [44.3, 130.0], [44.4, 130.0], [44.5, 130.0], [44.6, 130.0], [44.7, 130.0], [44.8, 130.0], [44.9, 130.0], [45.0, 130.0], [45.1, 130.0], [45.2, 130.0], [45.3, 130.0], [45.4, 131.0], [45.5, 131.0], [45.6, 131.0], [45.7, 131.0], [45.8, 131.0], [45.9, 131.0], [46.0, 131.0], [46.1, 131.0], [46.2, 131.0], [46.3, 131.0], [46.4, 131.0], [46.5, 132.0], [46.6, 132.0], [46.7, 132.0], [46.8, 132.0], [46.9, 132.0], [47.0, 132.0], [47.1, 132.0], [47.2, 132.0], [47.3, 132.0], [47.4, 132.0], [47.5, 133.0], [47.6, 133.0], [47.7, 133.0], [47.8, 133.0], [47.9, 133.0], [48.0, 133.0], [48.1, 133.0], [48.2, 133.0], [48.3, 133.0], [48.4, 133.0], [48.5, 134.0], [48.6, 134.0], [48.7, 134.0], [48.8, 134.0], [48.9, 134.0], [49.0, 134.0], [49.1, 134.0], [49.2, 134.0], [49.3, 134.0], [49.4, 134.0], [49.5, 135.0], [49.6, 135.0], [49.7, 135.0], [49.8, 135.0], [49.9, 135.0], [50.0, 135.0], [50.1, 135.0], [50.2, 135.0], [50.3, 135.0], [50.4, 135.0], [50.5, 136.0], [50.6, 136.0], [50.7, 136.0], [50.8, 136.0], [50.9, 136.0], [51.0, 136.0], [51.1, 136.0], [51.2, 136.0], [51.3, 136.0], [51.4, 137.0], [51.5, 137.0], [51.6, 137.0], [51.7, 137.0], [51.8, 137.0], [51.9, 137.0], [52.0, 137.0], [52.1, 137.0], [52.2, 137.0], [52.3, 138.0], [52.4, 138.0], [52.5, 138.0], [52.6, 138.0], [52.7, 138.0], [52.8, 138.0], [52.9, 138.0], [53.0, 138.0], [53.1, 138.0], [53.2, 139.0], [53.3, 139.0], [53.4, 139.0], [53.5, 139.0], [53.6, 139.0], [53.7, 139.0], [53.8, 139.0], [53.9, 139.0], [54.0, 140.0], [54.1, 140.0], [54.2, 140.0], [54.3, 140.0], [54.4, 140.0], [54.5, 140.0], [54.6, 140.0], [54.7, 140.0], [54.8, 141.0], [54.9, 141.0], [55.0, 141.0], [55.1, 141.0], [55.2, 141.0], [55.3, 141.0], [55.4, 141.0], [55.5, 141.0], [55.6, 142.0], [55.7, 142.0], [55.8, 142.0], [55.9, 142.0], [56.0, 142.0], [56.1, 142.0], [56.2, 142.0], [56.3, 142.0], [56.4, 143.0], [56.5, 143.0], [56.6, 143.0], [56.7, 143.0], [56.8, 143.0], [56.9, 143.0], [57.0, 143.0], [57.1, 144.0], [57.2, 144.0], [57.3, 144.0], [57.4, 144.0], [57.5, 144.0], [57.6, 144.0], [57.7, 144.0], [57.8, 145.0], [57.9, 145.0], [58.0, 145.0], [58.1, 145.0], [58.2, 145.0], [58.3, 145.0], [58.4, 145.0], [58.5, 146.0], [58.6, 146.0], [58.7, 146.0], [58.8, 146.0], [58.9, 146.0], [59.0, 146.0], [59.1, 146.0], [59.2, 147.0], [59.3, 147.0], [59.4, 147.0], [59.5, 147.0], [59.6, 147.0], [59.7, 147.0], [59.8, 148.0], [59.9, 148.0], [60.0, 148.0], [60.1, 148.0], [60.2, 148.0], [60.3, 148.0], [60.4, 149.0], [60.5, 149.0], [60.6, 149.0], [60.7, 149.0], [60.8, 149.0], [60.9, 149.0], [61.0, 150.0], [61.1, 150.0], [61.2, 150.0], [61.3, 150.0], [61.4, 150.0], [61.5, 151.0], [61.6, 151.0], [61.7, 151.0], [61.8, 151.0], [61.9, 151.0], [62.0, 151.0], [62.1, 152.0], [62.2, 152.0], [62.3, 152.0], [62.4, 152.0], [62.5, 152.0], [62.6, 153.0], [62.7, 153.0], [62.8, 153.0], [62.9, 153.0], [63.0, 153.0], [63.1, 154.0], [63.2, 154.0], [63.3, 154.0], [63.4, 154.0], [63.5, 155.0], [63.6, 155.0], [63.7, 155.0], [63.8, 155.0], [63.9, 155.0], [64.0, 156.0], [64.1, 156.0], [64.2, 156.0], [64.3, 156.0], [64.4, 156.0], [64.5, 157.0], [64.6, 157.0], [64.7, 157.0], [64.8, 157.0], [64.9, 158.0], [65.0, 158.0], [65.1, 158.0], [65.2, 158.0], [65.3, 158.0], [65.4, 159.0], [65.5, 159.0], [65.6, 159.0], [65.7, 159.0], [65.8, 160.0], [65.9, 160.0], [66.0, 160.0], [66.1, 160.0], [66.2, 161.0], [66.3, 161.0], [66.4, 161.0], [66.5, 162.0], [66.6, 162.0], [66.7, 162.0], [66.8, 163.0], [66.9, 163.0], [67.0, 163.0], [67.1, 163.0], [67.2, 164.0], [67.3, 164.0], [67.4, 164.0], [67.5, 165.0], [67.6, 165.0], [67.7, 165.0], [67.8, 165.0], [67.9, 166.0], [68.0, 166.0], [68.1, 166.0], [68.2, 167.0], [68.3, 167.0], [68.4, 167.0], [68.5, 168.0], [68.6, 168.0], [68.7, 169.0], [68.8, 169.0], [68.9, 169.0], [69.0, 170.0], [69.1, 170.0], [69.2, 171.0], [69.3, 171.0], [69.4, 171.0], [69.5, 172.0], [69.6, 172.0], [69.7, 173.0], [69.8, 173.0], [69.9, 174.0], [70.0, 174.0], [70.1, 175.0], [70.2, 175.0], [70.3, 175.0], [70.4, 176.0], [70.5, 176.0], [70.6, 177.0], [70.7, 177.0], [70.8, 178.0], [70.9, 179.0], [71.0, 179.0], [71.1, 180.0], [71.2, 180.0], [71.3, 181.0], [71.4, 181.0], [71.5, 182.0], [71.6, 183.0], [71.7, 183.0], [71.8, 184.0], [71.9, 185.0], [72.0, 186.0], [72.1, 186.0], [72.2, 187.0], [72.3, 188.0], [72.4, 189.0], [72.5, 190.0], [72.6, 191.0], [72.7, 192.0], [72.8, 193.0], [72.9, 194.0], [73.0, 195.0], [73.1, 196.0], [73.2, 197.0], [73.3, 198.0], [73.4, 200.0], [73.5, 201.0], [73.6, 202.0], [73.7, 204.0], [73.8, 205.0], [73.9, 207.0], [74.0, 209.0], [74.1, 211.0], [74.2, 214.0], [74.3, 216.0], [74.4, 219.0], [74.5, 222.0], [74.6, 226.0], [74.7, 231.0], [74.8, 237.0], [74.9, 244.0], [75.0, 252.0], [75.1, 263.0], [75.2, 276.0], [75.3, 293.0], [75.4, 310.0], [75.5, 330.0], [75.6, 345.0], [75.7, 358.0], [75.8, 369.0], [75.9, 380.0], [76.0, 397.0], [76.1, 420.0], [76.2, 446.0], [76.3, 496.0], [76.4, 1087.0], [76.5, 1094.0], [76.6, 1099.0], [76.7, 1102.0], [76.8, 1104.0], [76.9, 1106.0], [77.0, 1108.0], [77.1, 1109.0], [77.2, 1111.0], [77.3, 1112.0], [77.4, 1113.0], [77.5, 1114.0], [77.6, 1115.0], [77.7, 1116.0], [77.8, 1117.0], [77.9, 1118.0], [78.0, 1119.0], [78.1, 1120.0], [78.2, 1121.0], [78.3, 1122.0], [78.4, 1122.0], [78.5, 1123.0], [78.6, 1124.0], [78.7, 1124.0], [78.8, 1125.0], [78.9, 1126.0], [79.0, 1126.0], [79.1, 1127.0], [79.2, 1127.0], [79.3, 1128.0], [79.4, 1128.0], [79.5, 1129.0], [79.6, 1130.0], [79.7, 1130.0], [79.8, 1131.0], [79.9, 1131.0], [80.0, 1132.0], [80.1, 1132.0], [80.2, 1133.0], [80.3, 1134.0], [80.4, 1134.0], [80.5, 1135.0], [80.6, 1135.0], [80.7, 1136.0], [80.8, 1136.0], [80.9, 1137.0], [81.0, 1137.0], [81.1, 1138.0], [81.2, 1138.0], [81.3, 1138.0], [81.4, 1139.0], [81.5, 1139.0], [81.6, 1140.0], [81.7, 1140.0], [81.8, 1141.0], [81.9, 1141.0], [82.0, 1142.0], [82.1, 1142.0], [82.2, 1143.0], [82.3, 1143.0], [82.4, 1144.0], [82.5, 1144.0], [82.6, 1144.0], [82.7, 1145.0], [82.8, 1145.0], [82.9, 1146.0], [83.0, 1146.0], [83.1, 1147.0], [83.2, 1147.0], [83.3, 1147.0], [83.4, 1148.0], [83.5, 1148.0], [83.6, 1149.0], [83.7, 1149.0], [83.8, 1150.0], [83.9, 1150.0], [84.0, 1150.0], [84.1, 1151.0], [84.2, 1151.0], [84.3, 1152.0], [84.4, 1152.0], [84.5, 1152.0], [84.6, 1153.0], [84.7, 1153.0], [84.8, 1154.0], [84.9, 1154.0], [85.0, 1154.0], [85.1, 1155.0], [85.2, 1155.0], [85.3, 1156.0], [85.4, 1156.0], [85.5, 1157.0], [85.6, 1157.0], [85.7, 1157.0], [85.8, 1158.0], [85.9, 1158.0], [86.0, 1159.0], [86.1, 1159.0], [86.2, 1159.0], [86.3, 1160.0], [86.4, 1160.0], [86.5, 1161.0], [86.6, 1161.0], [86.7, 1161.0], [86.8, 1162.0], [86.9, 1162.0], [87.0, 1163.0], [87.1, 1163.0], [87.2, 1164.0], [87.3, 1164.0], [87.4, 1164.0], [87.5, 1165.0], [87.6, 1165.0], [87.7, 1166.0], [87.8, 1166.0], [87.9, 1166.0], [88.0, 1167.0], [88.1, 1167.0], [88.2, 1168.0], [88.3, 1168.0], [88.4, 1169.0], [88.5, 1169.0], [88.6, 1169.0], [88.7, 1170.0], [88.8, 1170.0], [88.9, 1171.0], [89.0, 1171.0], [89.1, 1171.0], [89.2, 1172.0], [89.3, 1172.0], [89.4, 1173.0], [89.5, 1173.0], [89.6, 1174.0], [89.7, 1174.0], [89.8, 1175.0], [89.9, 1175.0], [90.0, 1176.0], [90.1, 1176.0], [90.2, 1176.0], [90.3, 1177.0], [90.4, 1177.0], [90.5, 1178.0], [90.6, 1178.0], [90.7, 1179.0], [90.8, 1179.0], [90.9, 1180.0], [91.0, 1180.0], [91.1, 1181.0], [91.2, 1181.0], [91.3, 1182.0], [91.4, 1182.0], [91.5, 1183.0], [91.6, 1183.0], [91.7, 1184.0], [91.8, 1184.0], [91.9, 1185.0], [92.0, 1185.0], [92.1, 1186.0], [92.2, 1186.0], [92.3, 1187.0], [92.4, 1187.0], [92.5, 1188.0], [92.6, 1188.0], [92.7, 1189.0], [92.8, 1190.0], [92.9, 1190.0], [93.0, 1191.0], [93.1, 1191.0], [93.2, 1192.0], [93.3, 1193.0], [93.4, 1193.0], [93.5, 1194.0], [93.6, 1195.0], [93.7, 1195.0], [93.8, 1196.0], [93.9, 1197.0], [94.0, 1197.0], [94.1, 1198.0], [94.2, 1199.0], [94.3, 1200.0], [94.4, 1200.0], [94.5, 1201.0], [94.6, 1202.0], [94.7, 1203.0], [94.8, 1204.0], [94.9, 1204.0], [95.0, 1206.0], [95.1, 1207.0], [95.2, 1208.0], [95.3, 1209.0], [95.4, 1210.0], [95.5, 1211.0], [95.6, 1212.0], [95.7, 1213.0], [95.8, 1214.0], [95.9, 1216.0], [96.0, 1217.0], [96.1, 1219.0], [96.2, 1220.0], [96.3, 1222.0], [96.4, 1225.0], [96.5, 1227.0], [96.6, 1230.0], [96.7, 1233.0], [96.8, 1236.0], [96.9, 1240.0], [97.0, 1245.0], [97.1, 1252.0], [97.2, 1260.0], [97.3, 1280.0], [97.4, 1335.0], [97.5, 1393.0], [97.6, 1437.0], [97.7, 1502.0], [97.8, 2105.0], [97.9, 2115.0], [98.0, 2124.0], [98.1, 2131.0], [98.2, 2137.0], [98.3, 2142.0], [98.4, 2147.0], [98.5, 2152.0], [98.6, 2158.0], [98.7, 2163.0], [98.8, 2170.0], [98.9, 2177.0], [99.0, 2184.0], [99.1, 2191.0], [99.2, 2200.0], [99.3, 2214.0], [99.4, 2346.0], [99.5, 3001.0], [99.6, 3001.0], [99.7, 3002.0], [99.8, 3003.0], [99.9, 3016.0]], "isOverall": false, "label": "HTTP Request (가상머신조회)", "isController": false}], "supportsControllersDiscrimination": true, "maxX": 100.0, "title": "Response Time Percentiles"}},
        getOptions: function() {
            return {
                series: {
                    points: { show: false }
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendResponseTimePercentiles'
                },
                xaxis: {
                    tickDecimals: 1,
                    axisLabel: "Percentiles",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Percentile value in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : %x.2 percentile was %y ms"
                },
                selection: { mode: "xy" },
            };
        },
        createGraph: function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesResponseTimePercentiles"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotResponseTimesPercentiles"), dataset, options);
            // setup overview
            $.plot($("#overviewResponseTimesPercentiles"), dataset, prepareOverviewOptions(options));
        }
};

/**
 * @param elementId Id of element where we display message
 */
function setEmptyGraph(elementId) {
    $(function() {
        $(elementId).text("No graph series with filter="+seriesFilter);
    });
}

// Response times percentiles
function refreshResponseTimePercentiles() {
    var infos = responseTimePercentilesInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyResponseTimePercentiles");
        return;
    }
    if (isGraph($("#flotResponseTimesPercentiles"))){
        infos.createGraph();
    } else {
        var choiceContainer = $("#choicesResponseTimePercentiles");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotResponseTimesPercentiles", "#overviewResponseTimesPercentiles");
        $('#bodyResponseTimePercentiles .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
}

var responseTimeDistributionInfos = {
        data: {"result": {"minY": 1.0, "minX": 0.0, "maxY": 75792.0, "series": [{"data": [[0.0, 11175.0], [600.0, 11.0], [700.0, 4.0], [800.0, 1.0], [1000.0, 297.0], [1100.0, 20939.0], [1200.0, 3627.0], [1300.0, 197.0], [1400.0, 216.0], [1500.0, 61.0], [100.0, 75792.0], [1600.0, 2.0], [2000.0, 31.0], [2100.0, 1681.0], [2200.0, 240.0], [2300.0, 17.0], [2400.0, 12.0], [2500.0, 1.0], [3000.0, 634.0], [200.0, 2320.0], [4000.0, 51.0], [300.0, 794.0], [5000.0, 1.0], [400.0, 341.0], [500.0, 58.0]], "isOverall": false, "label": "HTTP Request (가상머신조회)", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 100, "maxX": 5000.0, "title": "Response Time Distribution"}},
        getOptions: function() {
            var granularity = this.data.result.granularity;
            return {
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendResponseTimeDistribution'
                },
                xaxis:{
                    axisLabel: "Response times in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of responses",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                bars : {
                    show: true,
                    barWidth: this.data.result.granularity
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: function(label, xval, yval, flotItem){
                        return yval + " responses for " + label + " were between " + xval + " and " + (xval + granularity) + " ms";
                    }
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotResponseTimeDistribution"), prepareData(data.result.series, $("#choicesResponseTimeDistribution")), options);
        }

};

// Response time distribution
function refreshResponseTimeDistribution() {
    var infos = responseTimeDistributionInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyResponseTimeDistribution");
        return;
    }
    if (isGraph($("#flotResponseTimeDistribution"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesResponseTimeDistribution");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        $('#footerResponseTimeDistribution .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};


var syntheticResponseTimeDistributionInfos = {
        data: {"result": {"minY": 686.0, "minX": 0.0, "ticks": [[0, "Requests having \nresponse time <= 500ms"], [1, "Requests having \nresponse time > 500ms and <= 1,500ms"], [2, "Requests having \nresponse time > 1,500ms"], [3, "Requests in error"]], "maxY": 90423.0, "series": [{"data": [[0.0, 90423.0]], "color": "#9ACD32", "isOverall": false, "label": "Requests having \nresponse time <= 500ms", "isController": false}, {"data": [[1.0, 25350.0]], "color": "yellow", "isOverall": false, "label": "Requests having \nresponse time > 500ms and <= 1,500ms", "isController": false}, {"data": [[2.0, 2044.0]], "color": "orange", "isOverall": false, "label": "Requests having \nresponse time > 1,500ms", "isController": false}, {"data": [[3.0, 686.0]], "color": "#FF6347", "isOverall": false, "label": "Requests in error", "isController": false}], "supportsControllersDiscrimination": false, "maxX": 3.0, "title": "Synthetic Response Times Distribution"}},
        getOptions: function() {
            return {
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendSyntheticResponseTimeDistribution'
                },
                xaxis:{
                    axisLabel: "Response times ranges",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                    tickLength:0,
                    min:-0.5,
                    max:3.5
                },
                yaxis: {
                    axisLabel: "Number of responses",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                bars : {
                    show: true,
                    align: "center",
                    barWidth: 0.25,
                    fill:.75
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: function(label, xval, yval, flotItem){
                        return yval + " " + label;
                    }
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var options = this.getOptions();
            prepareOptions(options, data);
            options.xaxis.ticks = data.result.ticks;
            $.plot($("#flotSyntheticResponseTimeDistribution"), prepareData(data.result.series, $("#choicesSyntheticResponseTimeDistribution")), options);
        }

};

// Response time distribution
function refreshSyntheticResponseTimeDistribution() {
    var infos = syntheticResponseTimeDistributionInfos;
    prepareSeries(infos.data, true);
    if (isGraph($("#flotSyntheticResponseTimeDistribution"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesSyntheticResponseTimeDistribution");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        $('#footerSyntheticResponseTimeDistribution .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var activeThreadsOverTimeInfos = {
        data: {"result": {"minY": 10.0, "minX": 1.76745E12, "maxY": 50.0, "series": [{"data": [[1.76745018E12, 20.0], [1.76745084E12, 50.0], [1.76745054E12, 50.0], [1.76745048E12, 45.32034771410177], [1.76745114E12, 50.0], [1.76745108E12, 50.0], [1.76745078E12, 50.0], [1.76745072E12, 50.0], [1.76745012E12, 15.362156987874876], [1.76745042E12, 40.0], [1.76745036E12, 35.440753752794556], [1.76745E12, 10.0], [1.76745102E12, 50.0], [1.76745006E12, 10.0], [1.76745096E12, 50.0], [1.76745066E12, 50.0], [1.7674506E12, 50.0], [1.76745024E12, 25.310583425066785], [1.7674503E12, 30.0], [1.7674512E12, 49.601802403204275], [1.7674509E12, 50.0]], "isOverall": false, "label": "bzm - Concurrency Thread Group-ThreadStarter", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.7674512E12, "title": "Active Threads Over Time"}},
        getOptions: function() {
            return {
                series: {
                    stack: true,
                    lines: {
                        show: true,
                        fill: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of active threads",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: {
                    noColumns: 6,
                    show: true,
                    container: '#legendActiveThreadsOverTime'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                selection: {
                    mode: 'xy'
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : At %x there were %y active threads"
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesActiveThreadsOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotActiveThreadsOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewActiveThreadsOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Active Threads Over Time
function refreshActiveThreadsOverTime(fixTimestamps) {
    var infos = activeThreadsOverTimeInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 32400000);
    }
    if(isGraph($("#flotActiveThreadsOverTime"))) {
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesActiveThreadsOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotActiveThreadsOverTime", "#overviewActiveThreadsOverTime");
        $('#footerActiveThreadsOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var timeVsThreadsInfos = {
        data: {"result": {"minY": 130.45676732565735, "minX": 1.0, "maxY": 2170.0, "series": [{"data": [[33.0, 1158.5], [2.0, 2145.0], [34.0, 1163.0], [37.0, 1159.0], [39.0, 1168.0], [40.0, 394.5670781893004], [42.0, 1149.6666666666667], [45.0, 1125.0], [44.0, 1134.5], [47.0, 1148.0], [46.0, 1161.0], [49.0, 1138.0], [48.0, 1141.0], [3.0, 2170.0], [50.0, 491.85401479819876], [4.0, 2146.0], [5.0, 2146.0], [6.0, 2167.0], [8.0, 2128.5], [10.0, 130.45676732565735], [15.0, 2144.0], [16.0, 2146.0], [1.0, 2161.0], [17.0, 2142.0], [18.0, 2130.0], [19.0, 2135.0], [20.0, 199.34652557907023], [21.0, 2123.0], [22.0, 2114.0], [23.0, 1159.0], [25.0, 1173.0], [26.0, 1183.0], [27.0, 1164.0], [30.0, 297.1586546486399], [31.0, 1171.75]], "isOverall": false, "label": "HTTP Request (가상머신조회)", "isController": false}, {"data": [[40.7975072361032, 404.90924280398565]], "isOverall": false, "label": "HTTP Request (가상머신조회)-Aggregated", "isController": false}], "supportsControllersDiscrimination": true, "maxX": 50.0, "title": "Time VS Threads"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    axisLabel: "Number of active threads",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Average response times in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: { noColumns: 2,show: true, container: '#legendTimeVsThreads' },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s: At %x.2 active threads, Average response time was %y.2 ms"
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesTimeVsThreads"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotTimesVsThreads"), dataset, options);
            // setup overview
            $.plot($("#overviewTimesVsThreads"), dataset, prepareOverviewOptions(options));
        }
};

// Time vs threads
function refreshTimeVsThreads(){
    var infos = timeVsThreadsInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyTimeVsThreads");
        return;
    }
    if(isGraph($("#flotTimesVsThreads"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesTimeVsThreads");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotTimesVsThreads", "#overviewTimesVsThreads");
        $('#footerTimeVsThreads .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var bytesThroughputOverTimeInfos = {
        data : {"result": {"minY": 7261.0, "minX": 1.76745E12, "maxY": 509861.3, "series": [{"data": [[1.76745018E12, 453706.35], [1.76745084E12, 480531.65], [1.76745054E12, 472845.4], [1.76745048E12, 497089.8], [1.76745114E12, 500267.65], [1.76745108E12, 481120.95], [1.76745078E12, 492339.8], [1.76745072E12, 485034.75], [1.76745012E12, 502628.35], [1.76745042E12, 466811.95], [1.76745036E12, 501373.35], [1.76745E12, 131937.0], [1.76745102E12, 484789.9], [1.76745006E12, 372923.2], [1.76745096E12, 479807.95], [1.76745066E12, 476785.7], [1.7674506E12, 498566.75], [1.76745024E12, 509861.3], [1.7674503E12, 460694.15], [1.7674512E12, 237346.8], [1.7674509E12, 495210.15]], "isOverall": false, "label": "Bytes received per second", "isController": false}, {"data": [[1.76745018E12, 24976.25], [1.76745084E12, 26420.5], [1.76745054E12, 25965.583333333332], [1.76745048E12, 27286.166666666668], [1.76745114E12, 27520.25], [1.76745108E12, 26257.083333333332], [1.76745078E12, 26963.75], [1.76745072E12, 26636.916666666668], [1.76745012E12, 27670.416666666668], [1.76745042E12, 25612.25], [1.76745036E12, 27524.666666666668], [1.76745E12, 7261.0], [1.76745102E12, 26619.25], [1.76745006E12, 20524.25], [1.76745096E12, 26274.75], [1.76745066E12, 26120.166666666668], [1.7674506E12, 27312.666666666668], [1.76745024E12, 28059.083333333332], [1.7674503E12, 25320.75], [1.7674512E12, 12852.5], [1.7674509E12, 27180.166666666668]], "isOverall": false, "label": "Bytes sent per second", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.7674512E12, "title": "Bytes Throughput Over Time"}},
        getOptions : function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity) ,
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Bytes / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendBytesThroughputOverTime'
                },
                selection: {
                    mode: "xy"
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s at %x was %y"
                }
            };
        },
        createGraph : function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesBytesThroughputOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotBytesThroughputOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewBytesThroughputOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Bytes throughput Over Time
function refreshBytesThroughputOverTime(fixTimestamps) {
    var infos = bytesThroughputOverTimeInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 32400000);
    }
    if(isGraph($("#flotBytesThroughputOverTime"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesBytesThroughputOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotBytesThroughputOverTime", "#overviewBytesThroughputOverTime");
        $('#footerBytesThroughputOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
}

var responseTimesOverTimeInfos = {
        data: {"result": {"minY": 128.26854439905378, "minX": 1.76745E12, "maxY": 672.3694926568763, "series": [{"data": [[1.76745018E12, 210.28738069989413], [1.76745084E12, 496.82705136758034], [1.76745054E12, 504.5972574911131], [1.76745048E12, 418.3512556342564], [1.76745114E12, 476.91379586604666], [1.76745108E12, 496.6532538499742], [1.76745078E12, 482.818683100875], [1.76745072E12, 502.14872895345053], [1.76745012E12, 130.2509572431399], [1.76745042E12, 409.12165867032223], [1.76745036E12, 323.09150431172156], [1.76745E12, 135.97083839611182], [1.76745102E12, 486.77797953119966], [1.76745006E12, 128.26854439905378], [1.76745096E12, 504.06062624916876], [1.76745066E12, 494.0385324174912], [1.7674506E12, 488.03735770402335], [1.76745024E12, 222.2924988205693], [1.7674503E12, 311.7433043478267], [1.7674512E12, 672.3694926568763], [1.7674509E12, 485.25395799676903]], "isOverall": false, "label": "HTTP Request (가상머신조회)", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.7674512E12, "title": "Response Time Over Time"}},
        getOptions: function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Average response time in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendResponseTimesOverTime'
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : at %x Average response time was %y ms"
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesResponseTimesOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotResponseTimesOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewResponseTimesOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Response Times Over Time
function refreshResponseTimeOverTime(fixTimestamps) {
    var infos = responseTimesOverTimeInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyResponseTimeOverTime");
        return;
    }
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 32400000);
    }
    if(isGraph($("#flotResponseTimesOverTime"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesResponseTimesOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotResponseTimesOverTime", "#overviewResponseTimesOverTime");
        $('#footerResponseTimesOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var latenciesOverTimeInfos = {
        data: {"result": {"minY": 123.88002580090316, "minX": 1.76745E12, "maxY": 582.3170894526024, "series": [{"data": [[1.76745018E12, 207.30540827147396], [1.76745084E12, 488.3560707138042], [1.76745054E12, 489.23514474352504], [1.76745048E12, 400.31068898905494], [1.76745114E12, 471.091331517385], [1.76745108E12, 449.0052988905462], [1.76745078E12, 451.8640934155043], [1.76745072E12, 486.7375371409706], [1.76745012E12, 127.53876834716021], [1.76745042E12, 388.70938999314507], [1.76745036E12, 307.2047269243062], [1.76745E12, 130.95200486026712], [1.76745102E12, 470.5906239683065], [1.76745006E12, 123.88002580090316], [1.76745096E12, 474.08960692871386], [1.76745066E12, 465.0070363544982], [1.7674506E12, 459.6677890011252], [1.76745024E12, 218.00518949520358], [1.7674503E12, 300.0241739130432], [1.7674512E12, 582.3170894526024], [1.7674509E12, 466.4326332794824]], "isOverall": false, "label": "HTTP Request (가상머신조회)", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.7674512E12, "title": "Latencies Over Time"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Average response latencies in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendLatenciesOverTime'
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : at %x Average latency was %y ms"
                }
            };
        },
        createGraph: function () {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesLatenciesOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotLatenciesOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewLatenciesOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Latencies Over Time
function refreshLatenciesOverTime(fixTimestamps) {
    var infos = latenciesOverTimeInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyLatenciesOverTime");
        return;
    }
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 32400000);
    }
    if(isGraph($("#flotLatenciesOverTime"))) {
        infos.createGraph();
    }else {
        var choiceContainer = $("#choicesLatenciesOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotLatenciesOverTime", "#overviewLatenciesOverTime");
        $('#footerLatenciesOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var connectTimeOverTimeInfos = {
        data: {"result": {"minY": 42.617861482381585, "minX": 1.76745E12, "maxY": 570.9582777036051, "series": [{"data": [[1.76745018E12, 125.90791799222339], [1.76745084E12, 392.080887258174], [1.76745054E12, 403.99373624513214], [1.76745048E12, 325.2828396651647], [1.76745114E12, 371.1982054157992], [1.76745108E12, 395.36032455704594], [1.76745078E12, 382.45977943561513], [1.76745072E12, 392.74050841861833], [1.76745012E12, 45.2865347798341], [1.76745042E12, 319.3250514050725], [1.76745036E12, 232.49584797189385], [1.76745E12, 42.617861482381585], [1.76745102E12, 386.4234070650377], [1.76745006E12, 44.96796387873581], [1.76745096E12, 402.35942704863425], [1.76745066E12, 391.7113419333222], [1.7674506E12, 390.2465929132588], [1.76745024E12, 138.13272527126864], [1.7674503E12, 222.84695652173954], [1.7674512E12, 570.9582777036051], [1.7674509E12, 383.80177705977337]], "isOverall": false, "label": "HTTP Request (가상머신조회)", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.7674512E12, "title": "Connect Time Over Time"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getConnectTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Average Connect Time in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendConnectTimeOverTime'
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : at %x Average connect time was %y ms"
                }
            };
        },
        createGraph: function () {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesConnectTimeOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotConnectTimeOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewConnectTimeOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Connect Time Over Time
function refreshConnectTimeOverTime(fixTimestamps) {
    var infos = connectTimeOverTimeInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyConnectTimeOverTime");
        return;
    }
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 32400000);
    }
    if(isGraph($("#flotConnectTimeOverTime"))) {
        infos.createGraph();
    }else {
        var choiceContainer = $("#choicesConnectTimeOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotConnectTimeOverTime", "#overviewConnectTimeOverTime");
        $('#footerConnectTimeOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var responseTimePercentilesOverTimeInfos = {
        data: {"result": {"minY": 61.0, "minX": 1.76745E12, "maxY": 2503.0, "series": [{"data": [[1.76745018E12, 2185.0], [1.76745084E12, 2247.0], [1.76745054E12, 2503.0], [1.76745048E12, 2288.0], [1.76745114E12, 2346.0], [1.76745108E12, 2397.0], [1.76745078E12, 2409.0], [1.76745072E12, 2303.0], [1.76745012E12, 1181.0], [1.76745042E12, 2366.0], [1.76745036E12, 2240.0], [1.76745E12, 845.0], [1.76745102E12, 2229.0], [1.76745006E12, 1122.0], [1.76745096E12, 2395.0], [1.76745066E12, 2437.0], [1.7674506E12, 2334.0], [1.76745024E12, 2193.0], [1.7674503E12, 2214.0], [1.7674512E12, 2445.0], [1.7674509E12, 2233.0]], "isOverall": false, "label": "Max", "isController": false}, {"data": [[1.76745018E12, 73.0], [1.76745084E12, 68.0], [1.76745054E12, 66.0], [1.76745048E12, 61.0], [1.76745114E12, 72.0], [1.76745108E12, 63.0], [1.76745078E12, 62.0], [1.76745072E12, 66.0], [1.76745012E12, 70.0], [1.76745042E12, 64.0], [1.76745036E12, 69.0], [1.76745E12, 69.0], [1.76745102E12, 71.0], [1.76745006E12, 73.0], [1.76745096E12, 70.0], [1.76745066E12, 66.0], [1.7674506E12, 66.0], [1.76745024E12, 63.0], [1.7674503E12, 72.0], [1.7674512E12, 70.0], [1.7674509E12, 65.0]], "isOverall": false, "label": "Min", "isController": false}, {"data": [[1.76745018E12, 190.0], [1.76745084E12, 1198.0], [1.76745054E12, 1190.0], [1.76745048E12, 1169.0], [1.76745114E12, 1187.0], [1.76745108E12, 1189.0], [1.76745078E12, 1189.0], [1.76745072E12, 1188.0], [1.76745012E12, 158.0], [1.76745042E12, 1161.0], [1.76745036E12, 1143.0], [1.76745E12, 155.5], [1.76745102E12, 1186.0], [1.76745006E12, 147.0], [1.76745096E12, 1191.0], [1.76745066E12, 1190.0], [1.7674506E12, 1179.0], [1.76745024E12, 214.20000000000073], [1.7674503E12, 1139.0], [1.7674512E12, 1197.9], [1.7674509E12, 1188.0]], "isOverall": false, "label": "90th percentile", "isController": false}, {"data": [[1.76745018E12, 1172.4399999999996], [1.76745084E12, 2191.17], [1.76745054E12, 2155.2], [1.76745048E12, 2142.0], [1.76745114E12, 2134.040000000001], [1.76745108E12, 2160.08], [1.76745078E12, 2158.0], [1.76745072E12, 2202.6800000000003], [1.76745012E12, 226.0], [1.76745042E12, 2138.0], [1.76745036E12, 2095.67], [1.76745E12, 405.1999999999998], [1.76745102E12, 2157.7200000000003], [1.76745006E12, 214.11999999999716], [1.76745096E12, 2178.5], [1.76745066E12, 2165.0], [1.7674506E12, 2156.1499999999996], [1.76745024E12, 1181.46], [1.7674503E12, 1511.9799999999996], [1.7674512E12, 2190.4499999999994], [1.7674509E12, 2150.0]], "isOverall": false, "label": "99th percentile", "isController": false}, {"data": [[1.76745018E12, 125.0], [1.76745084E12, 145.0], [1.76745054E12, 155.0], [1.76745048E12, 137.0], [1.76745114E12, 145.0], [1.76745108E12, 141.0], [1.76745078E12, 141.0], [1.76745072E12, 146.0], [1.76745012E12, 124.0], [1.76745042E12, 132.0], [1.76745036E12, 131.0], [1.76745E12, 120.0], [1.76745102E12, 142.0], [1.76745006E12, 122.0], [1.76745096E12, 146.0], [1.76745066E12, 147.0], [1.7674506E12, 147.0], [1.76745024E12, 125.0], [1.7674503E12, 130.0], [1.7674512E12, 158.5], [1.7674509E12, 136.0]], "isOverall": false, "label": "Median", "isController": false}, {"data": [[1.76745018E12, 1131.1999999999998], [1.76745084E12, 1236.0], [1.76745054E12, 1217.0], [1.76745048E12, 1195.0], [1.76745114E12, 1210.0], [1.76745108E12, 1215.0], [1.76745078E12, 1220.0], [1.76745072E12, 1217.0], [1.76745012E12, 170.69999999999982], [1.76745042E12, 1187.0], [1.76745036E12, 1170.0], [1.76745E12, 217.75], [1.76745102E12, 1208.5999999999995], [1.76745006E12, 157.0], [1.76745096E12, 1249.0], [1.76745066E12, 1215.0], [1.7674506E12, 1207.0], [1.76745024E12, 1131.0], [1.7674503E12, 1164.0], [1.7674512E12, 1238.0], [1.7674509E12, 1215.0]], "isOverall": false, "label": "95th percentile", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.7674512E12, "title": "Response Time Percentiles Over Time (successful requests only)"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true,
                        fill: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Response Time in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendResponseTimePercentilesOverTime'
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : at %x Response time was %y ms"
                }
            };
        },
        createGraph: function () {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesResponseTimePercentilesOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotResponseTimePercentilesOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewResponseTimePercentilesOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Response Time Percentiles Over Time
function refreshResponseTimePercentilesOverTime(fixTimestamps) {
    var infos = responseTimePercentilesOverTimeInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 32400000);
    }
    if(isGraph($("#flotResponseTimePercentilesOverTime"))) {
        infos.createGraph();
    }else {
        var choiceContainer = $("#choicesResponseTimePercentilesOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotResponseTimePercentilesOverTime", "#overviewResponseTimePercentilesOverTime");
        $('#footerResponseTimePercentilesOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};


var responseTimeVsRequestInfos = {
    data: {"result": {"minY": 107.0, "minX": 1.0, "maxY": 4024.0, "series": [{"data": [[2.0, 1123.5], [3.0, 1152.0], [5.0, 1154.0], [6.0, 145.5], [7.0, 1145.0], [8.0, 119.0], [9.0, 1131.0], [10.0, 1143.5], [11.0, 171.0], [12.0, 154.0], [13.0, 141.0], [14.0, 1133.0], [15.0, 175.0], [16.0, 122.0], [17.0, 1246.0], [18.0, 1139.5], [19.0, 139.5], [20.0, 144.0], [21.0, 146.0], [22.0, 1126.5], [23.0, 155.5], [24.0, 1140.0], [25.0, 131.5], [26.0, 147.0], [27.0, 1138.0], [28.0, 140.0], [29.0, 201.5], [30.0, 137.0], [31.0, 1142.0], [33.0, 1159.0], [32.0, 1147.0], [35.0, 1118.0], [34.0, 132.5], [37.0, 158.0], [36.0, 1122.5], [39.0, 152.5], [38.0, 124.5], [41.0, 1121.5], [40.0, 206.0], [43.0, 131.0], [42.0, 157.5], [44.0, 135.5], [45.0, 1122.0], [46.0, 1108.0], [47.0, 1118.5], [48.0, 156.0], [49.0, 1096.0], [50.0, 142.0], [51.0, 135.0], [53.0, 1130.0], [52.0, 125.0], [54.0, 156.0], [55.0, 181.0], [57.0, 133.5], [56.0, 1113.0], [59.0, 1139.0], [58.0, 1128.0], [60.0, 141.0], [61.0, 133.0], [63.0, 198.0], [62.0, 146.0], [64.0, 164.0], [67.0, 142.0], [66.0, 139.0], [65.0, 141.0], [69.0, 147.0], [70.0, 135.5], [71.0, 152.0], [68.0, 148.0], [74.0, 132.0], [73.0, 135.0], [75.0, 128.0], [72.0, 143.0], [77.0, 136.0], [79.0, 127.0], [78.0, 127.0], [76.0, 132.0], [83.0, 124.0], [81.0, 126.0], [82.0, 134.0], [80.0, 126.0], [87.0, 135.0], [84.0, 126.0], [85.0, 142.0], [86.0, 138.0], [88.0, 141.0], [90.0, 137.0], [89.0, 154.5], [91.0, 134.0], [93.0, 151.0], [92.0, 139.0], [95.0, 144.0], [94.0, 141.0], [99.0, 149.0], [96.0, 157.0], [97.0, 148.0], [98.0, 138.0], [102.0, 171.5], [101.0, 149.0], [100.0, 140.0], [103.0, 137.0], [105.0, 162.5], [106.0, 131.5], [104.0, 144.0], [107.0, 172.0], [109.0, 145.0], [108.0, 155.5], [110.0, 141.0], [111.0, 157.0], [113.0, 135.0], [115.0, 154.5], [114.0, 145.0], [112.0, 155.0], [119.0, 151.0], [118.0, 166.0], [116.0, 154.0], [117.0, 156.0], [122.0, 134.0], [120.0, 123.0], [123.0, 127.5], [121.0, 112.0], [124.0, 127.0], [126.0, 137.0], [125.0, 144.0], [134.0, 137.0], [135.0, 126.0], [131.0, 145.0], [128.0, 144.0], [130.0, 145.0], [132.0, 159.0], [129.0, 185.0], [140.0, 137.0], [141.0, 133.0], [138.0, 130.0], [142.0, 124.0], [143.0, 132.5], [137.0, 141.0], [139.0, 141.0], [136.0, 122.0], [145.0, 132.0], [144.0, 138.0], [148.0, 124.0], [147.0, 129.5], [151.0, 118.0], [150.0, 135.0], [149.0, 127.0], [146.0, 142.0], [152.0, 131.5], [155.0, 123.0], [157.0, 129.0], [154.0, 118.0], [153.0, 129.0], [156.0, 133.0], [159.0, 138.0], [158.0, 144.0], [162.0, 124.0], [160.0, 129.0], [166.0, 115.0], [167.0, 125.0], [161.0, 127.0], [164.0, 133.0], [165.0, 116.5], [163.0, 138.0], [175.0, 119.0], [169.0, 126.0], [172.0, 127.5], [168.0, 123.0], [173.0, 126.0], [174.0, 148.0], [171.0, 135.0], [170.0, 145.0], [183.0, 122.0], [180.0, 113.0], [176.0, 121.5], [178.0, 116.0], [181.0, 137.0], [182.0, 142.5], [189.0, 121.0], [190.0, 128.0], [185.0, 133.0], [191.0, 122.0], [187.0, 131.0], [188.0, 151.0], [184.0, 124.5], [199.0, 134.0], [198.0, 136.0], [194.0, 173.5], [196.0, 131.0], [195.0, 137.0], [193.0, 150.0], [202.0, 121.0], [204.0, 121.0], [207.0, 139.0], [206.0, 137.0], [205.0, 126.0], [203.0, 124.0], [200.0, 145.5], [214.0, 129.0], [212.0, 138.0], [209.0, 128.0], [208.0, 130.5], [216.0, 107.0], [221.0, 130.0], [222.0, 125.0], [223.0, 126.0], [226.0, 133.0], [225.0, 125.0], [234.0, 120.0], [232.0, 127.0], [235.0, 151.5], [236.0, 123.0], [243.0, 152.0], [246.0, 125.0], [241.0, 125.0], [254.0, 122.0], [250.0, 133.0], [252.0, 122.0], [267.0, 114.0], [262.0, 152.5], [270.0, 186.0], [260.0, 131.5], [263.0, 127.5], [259.0, 116.0], [264.0, 133.5], [265.0, 119.0], [274.0, 143.0], [282.0, 132.0], [280.0, 136.5], [283.0, 133.0], [276.0, 133.0], [286.0, 108.0], [275.0, 121.5], [294.0, 146.0], [299.0, 134.0], [293.0, 135.0], [298.0, 135.0], [300.0, 129.0], [317.0, 126.5], [318.0, 127.5], [328.0, 146.0], [320.0, 115.0], [349.0, 133.0], [338.0, 117.5], [347.0, 134.0], [359.0, 132.0], [356.0, 120.0], [371.0, 133.0], [1.0, 1632.0]], "isOverall": false, "label": "Successes", "isController": false}, {"data": [[9.0, 3018.5], [11.0, 3021.0], [12.0, 4020.0], [13.0, 3513.0], [14.0, 3002.0], [15.0, 3002.0], [17.0, 3013.0], [20.0, 3002.0], [23.0, 4018.0], [24.0, 3000.0], [26.0, 3002.0], [31.0, 3001.0], [33.0, 3023.0], [34.0, 3002.0], [35.0, 3016.0], [37.0, 3002.0], [39.0, 3015.0], [40.0, 3002.0], [41.0, 3002.0], [44.0, 3018.5], [47.0, 4016.0], [53.0, 3013.0], [52.0, 3035.0], [54.0, 4016.0], [57.0, 3048.0], [56.0, 3001.5], [58.0, 3001.0], [60.0, 3002.0], [62.0, 3002.0], [64.0, 3018.0], [67.0, 3001.0], [65.0, 3002.0], [66.0, 3002.0], [68.0, 3001.5], [71.0, 3001.0], [69.0, 3001.0], [74.0, 3002.0], [75.0, 3016.0], [73.0, 3018.0], [78.0, 3001.0], [76.0, 3002.0], [83.0, 3020.0], [82.0, 3002.0], [80.0, 3002.0], [81.0, 3021.0], [86.0, 3017.0], [87.0, 3001.0], [84.0, 3009.5], [90.0, 3002.0], [88.0, 3002.0], [89.0, 3015.0], [91.0, 3013.0], [92.0, 3002.0], [93.0, 3002.0], [95.0, 3018.5], [96.0, 3002.0], [98.0, 3002.0], [103.0, 3009.5], [101.0, 3002.0], [105.0, 3001.5], [104.0, 3001.5], [107.0, 3001.0], [109.0, 3027.0], [110.0, 3001.0], [113.0, 4014.0], [115.0, 3003.0], [114.0, 3001.0], [119.0, 3014.0], [118.0, 3015.0], [117.0, 4015.0], [120.0, 4024.0], [124.0, 3012.5], [134.0, 3001.5], [128.0, 3001.0], [130.0, 3001.5], [135.0, 3002.0], [137.0, 3001.0], [147.0, 3014.0], [144.0, 4021.0], [148.0, 3016.0], [155.0, 3025.0], [157.0, 3023.0], [153.0, 3014.0], [154.0, 4012.0], [158.0, 3001.5], [163.0, 3002.0], [167.0, 3011.0], [174.0, 3002.0], [171.0, 3001.5], [180.0, 3014.0], [182.0, 3017.5], [181.0, 3016.0], [190.0, 3001.0], [195.0, 3025.0], [207.0, 3001.5], [203.0, 3002.0], [214.0, 3009.0], [221.0, 3023.5], [236.0, 3020.0], [263.0, 3021.5], [275.0, 4018.0], [276.0, 3002.0], [298.0, 3022.0], [318.0, 3002.0], [1.0, 4016.0]], "isOverall": false, "label": "Failures", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 1000, "maxX": 371.0, "title": "Response Time Vs Request"}},
    getOptions: function() {
        return {
            series: {
                lines: {
                    show: false
                },
                points: {
                    show: true
                }
            },
            xaxis: {
                axisLabel: "Global number of requests per second",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 20,
            },
            yaxis: {
                axisLabel: "Median Response Time in ms",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 20,
            },
            legend: {
                noColumns: 2,
                show: true,
                container: '#legendResponseTimeVsRequest'
            },
            selection: {
                mode: 'xy'
            },
            grid: {
                hoverable: true // IMPORTANT! this is needed for tooltip to work
            },
            tooltip: true,
            tooltipOpts: {
                content: "%s : Median response time at %x req/s was %y ms"
            },
            colors: ["#9ACD32", "#FF6347"]
        };
    },
    createGraph: function () {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesResponseTimeVsRequest"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotResponseTimeVsRequest"), dataset, options);
        // setup overview
        $.plot($("#overviewResponseTimeVsRequest"), dataset, prepareOverviewOptions(options));

    }
};

// Response Time vs Request
function refreshResponseTimeVsRequest() {
    var infos = responseTimeVsRequestInfos;
    prepareSeries(infos.data);
    if (isGraph($("#flotResponseTimeVsRequest"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesResponseTimeVsRequest");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotResponseTimeVsRequest", "#overviewResponseTimeVsRequest");
        $('#footerResponseRimeVsRequest .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};


var latenciesVsRequestInfos = {
    data: {"result": {"minY": 0.0, "minX": 1.0, "maxY": 1632.0, "series": [{"data": [[2.0, 1121.5], [3.0, 1152.0], [5.0, 1154.0], [6.0, 139.5], [7.0, 1145.0], [8.0, 119.0], [9.0, 1129.0], [10.0, 1142.5], [11.0, 171.0], [12.0, 154.0], [13.0, 141.0], [14.0, 1132.0], [15.0, 175.0], [16.0, 120.0], [17.0, 1246.0], [18.0, 1137.0], [19.0, 138.5], [20.0, 143.0], [21.0, 144.0], [22.0, 1124.5], [23.0, 152.0], [24.0, 1137.0], [25.0, 129.5], [26.0, 146.0], [27.0, 1137.0], [28.0, 136.0], [29.0, 201.0], [30.0, 131.5], [31.0, 1142.0], [33.0, 1158.0], [32.0, 1146.5], [35.0, 1116.0], [34.0, 130.5], [37.0, 158.0], [36.0, 1122.0], [39.0, 152.5], [38.0, 124.0], [41.0, 1121.5], [40.0, 206.0], [43.0, 130.0], [42.0, 155.5], [44.0, 134.0], [45.0, 1120.0], [46.0, 1107.0], [47.0, 1118.0], [48.0, 153.5], [49.0, 1096.0], [50.0, 140.0], [51.0, 132.0], [53.0, 1129.0], [52.0, 124.0], [54.0, 153.0], [55.0, 181.0], [57.0, 131.0], [56.0, 1107.5], [59.0, 1139.0], [58.0, 1127.0], [60.0, 140.0], [61.0, 131.0], [63.0, 197.0], [62.0, 144.0], [64.0, 163.0], [67.0, 139.0], [66.0, 137.0], [65.0, 140.0], [69.0, 146.0], [70.0, 134.0], [71.0, 150.0], [68.0, 147.0], [74.0, 131.0], [73.0, 134.0], [75.0, 126.0], [72.0, 141.0], [77.0, 134.0], [79.0, 125.0], [78.0, 125.0], [76.0, 130.0], [83.0, 122.0], [81.0, 124.0], [82.0, 132.0], [80.0, 125.0], [87.0, 135.0], [84.0, 124.0], [85.0, 140.0], [86.0, 137.0], [88.0, 139.0], [90.0, 135.0], [89.0, 153.5], [91.0, 133.0], [93.0, 150.0], [92.0, 138.0], [95.0, 144.0], [94.0, 139.0], [99.0, 148.0], [96.0, 154.0], [97.0, 148.0], [98.0, 137.0], [102.0, 171.5], [101.0, 148.0], [100.0, 139.5], [103.0, 135.0], [105.0, 160.5], [106.0, 130.0], [104.0, 144.0], [107.0, 170.0], [109.0, 145.0], [108.0, 154.0], [110.0, 140.0], [111.0, 156.0], [113.0, 134.5], [115.0, 151.5], [114.0, 144.0], [112.0, 154.0], [119.0, 150.0], [118.0, 165.5], [116.0, 154.0], [117.0, 156.0], [122.0, 133.0], [120.0, 121.0], [123.0, 127.0], [121.0, 110.0], [124.0, 126.0], [126.0, 136.0], [125.0, 141.5], [134.0, 136.0], [135.0, 126.0], [131.0, 145.0], [128.0, 142.0], [130.0, 144.0], [132.0, 158.5], [129.0, 182.0], [140.0, 137.0], [141.0, 133.0], [138.0, 130.0], [142.0, 123.0], [143.0, 131.5], [137.0, 140.0], [139.0, 140.5], [136.0, 122.0], [145.0, 131.0], [144.0, 137.0], [148.0, 122.0], [147.0, 128.5], [151.0, 117.0], [150.0, 134.0], [149.0, 126.0], [146.0, 140.5], [152.0, 131.0], [155.0, 122.0], [157.0, 128.0], [154.0, 117.0], [153.0, 128.0], [156.0, 132.0], [159.0, 138.0], [158.0, 142.5], [162.0, 124.0], [160.0, 128.0], [166.0, 114.0], [167.0, 124.0], [161.0, 125.0], [164.0, 132.5], [165.0, 116.0], [163.0, 136.0], [175.0, 117.0], [169.0, 124.0], [172.0, 127.0], [168.0, 122.0], [173.0, 125.0], [174.0, 147.0], [171.0, 135.0], [170.0, 144.0], [183.0, 121.0], [180.0, 112.0], [176.0, 121.0], [178.0, 115.5], [181.0, 136.0], [182.0, 142.5], [189.0, 121.0], [190.0, 126.0], [185.0, 132.0], [191.0, 121.0], [187.0, 129.5], [188.0, 150.5], [184.0, 124.0], [199.0, 133.0], [198.0, 135.0], [194.0, 173.5], [196.0, 131.0], [195.0, 136.0], [193.0, 149.0], [202.0, 120.0], [204.0, 119.0], [207.0, 139.0], [206.0, 136.5], [205.0, 125.0], [203.0, 123.0], [200.0, 145.5], [214.0, 128.0], [212.0, 137.5], [209.0, 128.0], [208.0, 130.0], [216.0, 106.0], [221.0, 129.0], [222.0, 124.5], [223.0, 125.0], [226.0, 132.5], [225.0, 125.0], [234.0, 120.0], [232.0, 126.0], [235.0, 150.0], [236.0, 123.0], [243.0, 151.0], [246.0, 123.0], [241.0, 125.0], [254.0, 122.0], [250.0, 132.0], [252.0, 120.5], [267.0, 113.0], [262.0, 151.0], [270.0, 184.5], [260.0, 131.0], [263.0, 127.0], [259.0, 115.0], [264.0, 133.5], [265.0, 118.0], [274.0, 143.0], [282.0, 132.0], [280.0, 136.0], [283.0, 132.0], [276.0, 132.0], [286.0, 108.0], [275.0, 121.0], [294.0, 146.0], [299.0, 134.0], [293.0, 134.0], [298.0, 135.0], [300.0, 128.5], [317.0, 126.0], [318.0, 127.0], [328.0, 146.0], [320.0, 114.0], [349.0, 133.0], [338.0, 117.0], [347.0, 134.0], [359.0, 131.0], [356.0, 120.0], [371.0, 132.0], [1.0, 1632.0]], "isOverall": false, "label": "Successes", "isController": false}, {"data": [[9.0, 0.0], [11.0, 0.0], [12.0, 0.0], [13.0, 0.0], [14.0, 0.0], [15.0, 0.0], [17.0, 0.0], [20.0, 0.0], [23.0, 0.0], [24.0, 0.0], [26.0, 0.0], [31.0, 0.0], [33.0, 0.0], [34.0, 0.0], [35.0, 0.0], [37.0, 0.0], [39.0, 0.0], [40.0, 0.0], [41.0, 0.0], [44.0, 0.0], [47.0, 0.0], [53.0, 0.0], [52.0, 0.0], [54.0, 0.0], [57.0, 0.0], [56.0, 0.0], [58.0, 0.0], [60.0, 0.0], [62.0, 0.0], [64.0, 0.0], [67.0, 0.0], [65.0, 0.0], [66.0, 0.0], [68.0, 0.0], [71.0, 0.0], [69.0, 0.0], [74.0, 0.0], [75.0, 0.0], [73.0, 0.0], [78.0, 0.0], [76.0, 0.0], [83.0, 0.0], [82.0, 0.0], [80.0, 0.0], [81.0, 0.0], [86.0, 0.0], [87.0, 0.0], [84.0, 0.0], [90.0, 0.0], [88.0, 0.0], [89.0, 0.0], [91.0, 0.0], [92.0, 0.0], [93.0, 0.0], [95.0, 0.0], [96.0, 0.0], [98.0, 0.0], [103.0, 0.0], [101.0, 0.0], [105.0, 0.0], [104.0, 0.0], [107.0, 0.0], [109.0, 0.0], [110.0, 0.0], [113.0, 0.0], [115.0, 0.0], [114.0, 0.0], [119.0, 0.0], [118.0, 0.0], [117.0, 0.0], [120.0, 0.0], [124.0, 0.0], [134.0, 0.0], [128.0, 0.0], [130.0, 0.0], [135.0, 0.0], [137.0, 0.0], [147.0, 0.0], [144.0, 0.0], [148.0, 0.0], [155.0, 0.0], [157.0, 0.0], [153.0, 0.0], [154.0, 0.0], [158.0, 0.0], [163.0, 0.0], [167.0, 0.0], [174.0, 0.0], [171.0, 0.0], [180.0, 0.0], [182.0, 0.0], [181.0, 0.0], [190.0, 0.0], [195.0, 0.0], [207.0, 0.0], [203.0, 0.0], [214.0, 0.0], [221.0, 0.0], [236.0, 0.0], [263.0, 0.0], [275.0, 0.0], [276.0, 0.0], [298.0, 0.0], [318.0, 0.0], [1.0, 0.0]], "isOverall": false, "label": "Failures", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 1000, "maxX": 371.0, "title": "Latencies Vs Request"}},
    getOptions: function() {
        return{
            series: {
                lines: {
                    show: false
                },
                points: {
                    show: true
                }
            },
            xaxis: {
                axisLabel: "Global number of requests per second",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 20,
            },
            yaxis: {
                axisLabel: "Median Latency in ms",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 20,
            },
            legend: { noColumns: 2,show: true, container: '#legendLatencyVsRequest' },
            selection: {
                mode: 'xy'
            },
            grid: {
                hoverable: true // IMPORTANT! this is needed for tooltip to work
            },
            tooltip: true,
            tooltipOpts: {
                content: "%s : Median Latency time at %x req/s was %y ms"
            },
            colors: ["#9ACD32", "#FF6347"]
        };
    },
    createGraph: function () {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesLatencyVsRequest"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotLatenciesVsRequest"), dataset, options);
        // setup overview
        $.plot($("#overviewLatenciesVsRequest"), dataset, prepareOverviewOptions(options));
    }
};

// Latencies vs Request
function refreshLatenciesVsRequest() {
        var infos = latenciesVsRequestInfos;
        prepareSeries(infos.data);
        if(isGraph($("#flotLatenciesVsRequest"))){
            infos.createGraph();
        }else{
            var choiceContainer = $("#choicesLatencyVsRequest");
            createLegend(choiceContainer, infos);
            infos.createGraph();
            setGraphZoomable("#flotLatenciesVsRequest", "#overviewLatenciesVsRequest");
            $('#footerLatenciesVsRequest .legendColorBox > div').each(function(i){
                $(this).clone().prependTo(choiceContainer.find("li").eq(i));
            });
        }
};

var hitsPerSecondInfos = {
        data: {"result": {"minY": 27.6, "minX": 1.76745E12, "maxY": 106.15, "series": [{"data": [[1.76745018E12, 94.3], [1.76745084E12, 99.93333333333334], [1.76745054E12, 98.45], [1.76745048E12, 103.7], [1.76745114E12, 104.01666666666667], [1.76745108E12, 100.65], [1.76745078E12, 102.76666666666667], [1.76745072E12, 100.96666666666667], [1.76745012E12, 104.63333333333334], [1.76745042E12, 97.26666666666667], [1.76745036E12, 104.53333333333333], [1.76745E12, 27.6], [1.76745102E12, 100.96666666666667], [1.76745006E12, 77.51666666666667], [1.76745096E12, 100.06666666666666], [1.76745066E12, 99.51666666666667], [1.7674506E12, 103.91666666666667], [1.76745024E12, 106.15], [1.7674503E12, 95.83333333333333], [1.7674512E12, 49.1], [1.7674509E12, 103.16666666666667]], "isOverall": false, "label": "hitsPerSecond", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.7674512E12, "title": "Hits Per Second"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of hits / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: "#legendHitsPerSecond"
                },
                selection: {
                    mode : 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s at %x was %y.2 hits/sec"
                }
            };
        },
        createGraph: function createGraph() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesHitsPerSecond"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotHitsPerSecond"), dataset, options);
            // setup overview
            $.plot($("#overviewHitsPerSecond"), dataset, prepareOverviewOptions(options));
        }
};

// Hits per second
function refreshHitsPerSecond(fixTimestamps) {
    var infos = hitsPerSecondInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 32400000);
    }
    if (isGraph($("#flotHitsPerSecond"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesHitsPerSecond");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotHitsPerSecond", "#overviewHitsPerSecond");
        $('#footerHitsPerSecond .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
}

var codesPerSecondInfos = {
        data: {"result": {"minY": 0.03333333333333333, "minX": 1.76745E12, "maxY": 105.88333333333334, "series": [{"data": [[1.76745018E12, 94.25], [1.76745084E12, 99.7], [1.76745054E12, 97.98333333333333], [1.76745048E12, 102.96666666666667], [1.76745114E12, 103.85], [1.76745108E12, 99.08333333333333], [1.76745078E12, 101.75], [1.76745072E12, 100.51666666666667], [1.76745012E12, 104.41666666666667], [1.76745042E12, 96.65], [1.76745036E12, 103.86666666666666], [1.76745E12, 27.4], [1.76745102E12, 100.45], [1.76745006E12, 77.45], [1.76745096E12, 99.15], [1.76745066E12, 98.56666666666666], [1.7674506E12, 103.06666666666666], [1.76745024E12, 105.88333333333334], [1.7674503E12, 95.55], [1.7674512E12, 48.5], [1.7674509E12, 102.56666666666666]], "isOverall": false, "label": "200", "isController": false}, {"data": [[1.76745018E12, 0.05], [1.76745084E12, 0.23333333333333334], [1.76745054E12, 0.4666666666666667], [1.76745048E12, 0.5666666666666667], [1.76745114E12, 0.16666666666666666], [1.76745108E12, 1.5666666666666667], [1.76745078E12, 1.0166666666666666], [1.76745072E12, 0.45], [1.76745012E12, 0.05], [1.76745042E12, 0.6166666666666667], [1.76745036E12, 0.5], [1.76745E12, 0.03333333333333333], [1.76745102E12, 0.5166666666666667], [1.76745006E12, 0.06666666666666667], [1.76745096E12, 0.9166666666666666], [1.76745066E12, 0.9166666666666666], [1.7674506E12, 0.8833333333333333], [1.76745024E12, 0.1], [1.7674503E12, 0.2833333333333333], [1.7674512E12, 1.4333333333333333], [1.7674509E12, 0.6]], "isOverall": false, "label": "Non HTTP response code: org.apache.http.conn.ConnectTimeoutException", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.7674512E12, "title": "Codes Per Second"}},
        getOptions: function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of responses / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: "#legendCodesPerSecond"
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "Number of Response Codes %s at %x was %y.2 responses / sec"
                }
            };
        },
    createGraph: function() {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesCodesPerSecond"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotCodesPerSecond"), dataset, options);
        // setup overview
        $.plot($("#overviewCodesPerSecond"), dataset, prepareOverviewOptions(options));
    }
};

// Codes per second
function refreshCodesPerSecond(fixTimestamps) {
    var infos = codesPerSecondInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 32400000);
    }
    if(isGraph($("#flotCodesPerSecond"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesCodesPerSecond");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotCodesPerSecond", "#overviewCodesPerSecond");
        $('#footerCodesPerSecond .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var transactionsPerSecondInfos = {
        data: {"result": {"minY": 0.03333333333333333, "minX": 1.76745E12, "maxY": 105.88333333333334, "series": [{"data": [[1.76745018E12, 94.25], [1.76745084E12, 99.7], [1.76745054E12, 97.98333333333333], [1.76745048E12, 102.96666666666667], [1.76745114E12, 103.85], [1.76745108E12, 99.08333333333333], [1.76745078E12, 101.75], [1.76745072E12, 100.51666666666667], [1.76745012E12, 104.41666666666667], [1.76745042E12, 96.65], [1.76745036E12, 103.86666666666666], [1.76745E12, 27.4], [1.76745102E12, 100.45], [1.76745006E12, 77.45], [1.76745096E12, 99.15], [1.76745066E12, 98.56666666666666], [1.7674506E12, 103.06666666666666], [1.76745024E12, 105.88333333333334], [1.7674503E12, 95.55], [1.7674512E12, 48.5], [1.7674509E12, 102.56666666666666]], "isOverall": false, "label": "HTTP Request (가상머신조회)-success", "isController": false}, {"data": [[1.76745018E12, 0.05], [1.76745084E12, 0.23333333333333334], [1.76745054E12, 0.4666666666666667], [1.76745048E12, 0.5666666666666667], [1.76745114E12, 0.16666666666666666], [1.76745108E12, 1.5666666666666667], [1.76745078E12, 1.0166666666666666], [1.76745072E12, 0.45], [1.76745012E12, 0.05], [1.76745042E12, 0.6166666666666667], [1.76745036E12, 0.5], [1.76745E12, 0.03333333333333333], [1.76745102E12, 0.5166666666666667], [1.76745006E12, 0.06666666666666667], [1.76745096E12, 0.9166666666666666], [1.76745066E12, 0.9166666666666666], [1.7674506E12, 0.8833333333333333], [1.76745024E12, 0.1], [1.7674503E12, 0.2833333333333333], [1.7674512E12, 1.4333333333333333], [1.7674509E12, 0.6]], "isOverall": false, "label": "HTTP Request (가상머신조회)-failure", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.7674512E12, "title": "Transactions Per Second"}},
        getOptions: function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of transactions / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: "#legendTransactionsPerSecond"
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s at %x was %y transactions / sec"
                }
            };
        },
    createGraph: function () {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesTransactionsPerSecond"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotTransactionsPerSecond"), dataset, options);
        // setup overview
        $.plot($("#overviewTransactionsPerSecond"), dataset, prepareOverviewOptions(options));
    }
};

// Transactions per second
function refreshTransactionsPerSecond(fixTimestamps) {
    var infos = transactionsPerSecondInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyTransactionsPerSecond");
        return;
    }
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 32400000);
    }
    if(isGraph($("#flotTransactionsPerSecond"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesTransactionsPerSecond");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotTransactionsPerSecond", "#overviewTransactionsPerSecond");
        $('#footerTransactionsPerSecond .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var totalTPSInfos = {
        data: {"result": {"minY": 0.03333333333333333, "minX": 1.76745E12, "maxY": 105.88333333333334, "series": [{"data": [[1.76745018E12, 94.25], [1.76745084E12, 99.7], [1.76745054E12, 97.98333333333333], [1.76745048E12, 102.96666666666667], [1.76745114E12, 103.85], [1.76745108E12, 99.08333333333333], [1.76745078E12, 101.75], [1.76745072E12, 100.51666666666667], [1.76745012E12, 104.41666666666667], [1.76745042E12, 96.65], [1.76745036E12, 103.86666666666666], [1.76745E12, 27.4], [1.76745102E12, 100.45], [1.76745006E12, 77.45], [1.76745096E12, 99.15], [1.76745066E12, 98.56666666666666], [1.7674506E12, 103.06666666666666], [1.76745024E12, 105.88333333333334], [1.7674503E12, 95.55], [1.7674512E12, 48.5], [1.7674509E12, 102.56666666666666]], "isOverall": false, "label": "Transaction-success", "isController": false}, {"data": [[1.76745018E12, 0.05], [1.76745084E12, 0.23333333333333334], [1.76745054E12, 0.4666666666666667], [1.76745048E12, 0.5666666666666667], [1.76745114E12, 0.16666666666666666], [1.76745108E12, 1.5666666666666667], [1.76745078E12, 1.0166666666666666], [1.76745072E12, 0.45], [1.76745012E12, 0.05], [1.76745042E12, 0.6166666666666667], [1.76745036E12, 0.5], [1.76745E12, 0.03333333333333333], [1.76745102E12, 0.5166666666666667], [1.76745006E12, 0.06666666666666667], [1.76745096E12, 0.9166666666666666], [1.76745066E12, 0.9166666666666666], [1.7674506E12, 0.8833333333333333], [1.76745024E12, 0.1], [1.7674503E12, 0.2833333333333333], [1.7674512E12, 1.4333333333333333], [1.7674509E12, 0.6]], "isOverall": false, "label": "Transaction-failure", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.7674512E12, "title": "Total Transactions Per Second"}},
        getOptions: function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of transactions / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: "#legendTotalTPS"
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s at %x was %y transactions / sec"
                },
                colors: ["#9ACD32", "#FF6347"]
            };
        },
    createGraph: function () {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesTotalTPS"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotTotalTPS"), dataset, options);
        // setup overview
        $.plot($("#overviewTotalTPS"), dataset, prepareOverviewOptions(options));
    }
};

// Total Transactions per second
function refreshTotalTPS(fixTimestamps) {
    var infos = totalTPSInfos;
    // We want to ignore seriesFilter
    prepareSeries(infos.data, false, true);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 32400000);
    }
    if(isGraph($("#flotTotalTPS"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesTotalTPS");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotTotalTPS", "#overviewTotalTPS");
        $('#footerTotalTPS .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

// Collapse the graph matching the specified DOM element depending the collapsed
// status
function collapse(elem, collapsed){
    if(collapsed){
        $(elem).parent().find(".fa-chevron-up").removeClass("fa-chevron-up").addClass("fa-chevron-down");
    } else {
        $(elem).parent().find(".fa-chevron-down").removeClass("fa-chevron-down").addClass("fa-chevron-up");
        if (elem.id == "bodyBytesThroughputOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshBytesThroughputOverTime(true);
            }
            document.location.href="#bytesThroughputOverTime";
        } else if (elem.id == "bodyLatenciesOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshLatenciesOverTime(true);
            }
            document.location.href="#latenciesOverTime";
        } else if (elem.id == "bodyCustomGraph") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshCustomGraph(true);
            }
            document.location.href="#responseCustomGraph";
        } else if (elem.id == "bodyConnectTimeOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshConnectTimeOverTime(true);
            }
            document.location.href="#connectTimeOverTime";
        } else if (elem.id == "bodyResponseTimePercentilesOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshResponseTimePercentilesOverTime(true);
            }
            document.location.href="#responseTimePercentilesOverTime";
        } else if (elem.id == "bodyResponseTimeDistribution") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshResponseTimeDistribution();
            }
            document.location.href="#responseTimeDistribution" ;
        } else if (elem.id == "bodySyntheticResponseTimeDistribution") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshSyntheticResponseTimeDistribution();
            }
            document.location.href="#syntheticResponseTimeDistribution" ;
        } else if (elem.id == "bodyActiveThreadsOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshActiveThreadsOverTime(true);
            }
            document.location.href="#activeThreadsOverTime";
        } else if (elem.id == "bodyTimeVsThreads") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshTimeVsThreads();
            }
            document.location.href="#timeVsThreads" ;
        } else if (elem.id == "bodyCodesPerSecond") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshCodesPerSecond(true);
            }
            document.location.href="#codesPerSecond";
        } else if (elem.id == "bodyTransactionsPerSecond") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshTransactionsPerSecond(true);
            }
            document.location.href="#transactionsPerSecond";
        } else if (elem.id == "bodyTotalTPS") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshTotalTPS(true);
            }
            document.location.href="#totalTPS";
        } else if (elem.id == "bodyResponseTimeVsRequest") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshResponseTimeVsRequest();
            }
            document.location.href="#responseTimeVsRequest";
        } else if (elem.id == "bodyLatenciesVsRequest") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshLatenciesVsRequest();
            }
            document.location.href="#latencyVsRequest";
        }
    }
}

/*
 * Activates or deactivates all series of the specified graph (represented by id parameter)
 * depending on checked argument.
 */
function toggleAll(id, checked){
    var placeholder = document.getElementById(id);

    var cases = $(placeholder).find(':checkbox');
    cases.prop('checked', checked);
    $(cases).parent().children().children().toggleClass("legend-disabled", !checked);

    var choiceContainer;
    if ( id == "choicesBytesThroughputOverTime"){
        choiceContainer = $("#choicesBytesThroughputOverTime");
        refreshBytesThroughputOverTime(false);
    } else if(id == "choicesResponseTimesOverTime"){
        choiceContainer = $("#choicesResponseTimesOverTime");
        refreshResponseTimeOverTime(false);
    }else if(id == "choicesResponseCustomGraph"){
        choiceContainer = $("#choicesResponseCustomGraph");
        refreshCustomGraph(false);
    } else if ( id == "choicesLatenciesOverTime"){
        choiceContainer = $("#choicesLatenciesOverTime");
        refreshLatenciesOverTime(false);
    } else if ( id == "choicesConnectTimeOverTime"){
        choiceContainer = $("#choicesConnectTimeOverTime");
        refreshConnectTimeOverTime(false);
    } else if ( id == "choicesResponseTimePercentilesOverTime"){
        choiceContainer = $("#choicesResponseTimePercentilesOverTime");
        refreshResponseTimePercentilesOverTime(false);
    } else if ( id == "choicesResponseTimePercentiles"){
        choiceContainer = $("#choicesResponseTimePercentiles");
        refreshResponseTimePercentiles();
    } else if(id == "choicesActiveThreadsOverTime"){
        choiceContainer = $("#choicesActiveThreadsOverTime");
        refreshActiveThreadsOverTime(false);
    } else if ( id == "choicesTimeVsThreads"){
        choiceContainer = $("#choicesTimeVsThreads");
        refreshTimeVsThreads();
    } else if ( id == "choicesSyntheticResponseTimeDistribution"){
        choiceContainer = $("#choicesSyntheticResponseTimeDistribution");
        refreshSyntheticResponseTimeDistribution();
    } else if ( id == "choicesResponseTimeDistribution"){
        choiceContainer = $("#choicesResponseTimeDistribution");
        refreshResponseTimeDistribution();
    } else if ( id == "choicesHitsPerSecond"){
        choiceContainer = $("#choicesHitsPerSecond");
        refreshHitsPerSecond(false);
    } else if(id == "choicesCodesPerSecond"){
        choiceContainer = $("#choicesCodesPerSecond");
        refreshCodesPerSecond(false);
    } else if ( id == "choicesTransactionsPerSecond"){
        choiceContainer = $("#choicesTransactionsPerSecond");
        refreshTransactionsPerSecond(false);
    } else if ( id == "choicesTotalTPS"){
        choiceContainer = $("#choicesTotalTPS");
        refreshTotalTPS(false);
    } else if ( id == "choicesResponseTimeVsRequest"){
        choiceContainer = $("#choicesResponseTimeVsRequest");
        refreshResponseTimeVsRequest();
    } else if ( id == "choicesLatencyVsRequest"){
        choiceContainer = $("#choicesLatencyVsRequest");
        refreshLatenciesVsRequest();
    }
    var color = checked ? "black" : "#818181";
    if(choiceContainer != null) {
        choiceContainer.find("label").each(function(){
            this.style.color = color;
        });
    }
}

