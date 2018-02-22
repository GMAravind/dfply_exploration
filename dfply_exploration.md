

```python
from dfply import *
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
```

# Manufacturers and Products Table


```python
manu = pd.read_csv("manufacturers.csv")
prod = pd.read_csv("products.csv")
```

## Print the first five rows of a table


```python
prod >> head(5) # prod %>% head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prd_id</th>
      <th>name</th>
      <th>price</th>
      <th>mfr_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Hard drive</td>
      <td>240</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Memory</td>
      <td>120</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ZIP drive</td>
      <td>150</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Floppy disk</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Monitor</td>
      <td>240</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## Get a unique list of product names


```python
prod >> distinct(X.name) # prod %>% distinct(name)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prd_id</th>
      <th>name</th>
      <th>price</th>
      <th>mfr_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Hard drive</td>
      <td>240</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Memory</td>
      <td>120</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ZIP drive</td>
      <td>150</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Floppy disk</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Monitor</td>
      <td>240</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>DVD drive</td>
      <td>180</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>CD drive</td>
      <td>90</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Printer</td>
      <td>270</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Toner cartridge</td>
      <td>66</td>
      <td>3</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>DVD burner</td>
      <td>180</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



### As you can see, unlike dplyr, dfply.distinct outputs all columns and not just the "name" column

## Print first 5 records of the manufacturer table


```python
manu >> head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mfr_id</th>
      <th>mfr_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Sony</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Creative Labs</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Hewlett-Packard</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Iomega</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Fujitsu</td>
    </tr>
  </tbody>
</table>
</div>



## Filter for products with price > 100


```python
prod >> mask(X.price > 100) # prod %>% filter(price > 100)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prd_id</th>
      <th>name</th>
      <th>price</th>
      <th>mfr_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Hard drive</td>
      <td>240</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Memory</td>
      <td>120</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ZIP drive</td>
      <td>150</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Monitor</td>
      <td>240</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>DVD drive</td>
      <td>180</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Printer</td>
      <td>270</td>
      <td>3</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>DVD burner</td>
      <td>180</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



## Merge Product with manufacturers dataset


```python
prod_manu = prod >> left_join(manu, by = "mfr_id") #prod %>% left_join(manu, by = "mfr_id")
prod_manu
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prd_id</th>
      <th>name</th>
      <th>price</th>
      <th>mfr_id</th>
      <th>mfr_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Hard drive</td>
      <td>240</td>
      <td>5</td>
      <td>Fujitsu</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Memory</td>
      <td>120</td>
      <td>6</td>
      <td>Winchester</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ZIP drive</td>
      <td>150</td>
      <td>4</td>
      <td>Iomega</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Floppy disk</td>
      <td>5</td>
      <td>6</td>
      <td>Winchester</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Monitor</td>
      <td>240</td>
      <td>1</td>
      <td>Sony</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>DVD drive</td>
      <td>180</td>
      <td>2</td>
      <td>Creative Labs</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>CD drive</td>
      <td>90</td>
      <td>2</td>
      <td>Creative Labs</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Printer</td>
      <td>270</td>
      <td>3</td>
      <td>Hewlett-Packard</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Toner cartridge</td>
      <td>66</td>
      <td>3</td>
      <td>Hewlett-Packard</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>DVD burner</td>
      <td>180</td>
      <td>2</td>
      <td>Creative Labs</td>
    </tr>
  </tbody>
</table>
</div>



### Names have to be consistent to join

## Filter for manufacturers with average product price of greater than 150



```python
manu_150 = prod_manu >> group_by(X.mfr_id,X.mfr_name) >> summarize(avg_price = mean(X.price)) >> mask(X.avg_price >= 150)
# prod_manu %>% group_by(mfr_id,mfr_name) %>% summarise(avg_price = mean(price)) %>% filter(avg_price >= 150)
```


```python
manu_150
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mfr_name</th>
      <th>mfr_id</th>
      <th>avg_price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sony</td>
      <td>1</td>
      <td>240.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Creative Labs</td>
      <td>2</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Hewlett-Packard</td>
      <td>3</td>
      <td>168.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Iomega</td>
      <td>4</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Fujitsu</td>
      <td>5</td>
      <td>240.0</td>
    </tr>
  </tbody>
</table>
</div>



# Baseball Dataframe


```python
baseball = pd.read_csv("baseball.csv",names = ["Player_Name","Team_Name","Bats","Hits"])
baseball >> head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Player_Name</th>
      <th>Team_Name</th>
      <th>Bats</th>
      <th>Hits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A. J. Pierzynski</td>
      <td>White Sox</td>
      <td>479</td>
      <td>133</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aaron Hill</td>
      <td>Diamondbacks</td>
      <td>609</td>
      <td>184</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Adam Dunn</td>
      <td>White Sox</td>
      <td>539</td>
      <td>110</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Adam Jones</td>
      <td>Orioles</td>
      <td>648</td>
      <td>186</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Adam LaRoche</td>
      <td>Nationals</td>
      <td>571</td>
      <td>155</td>
    </tr>
  </tbody>
</table>
</div>



## Filter for teams with 7 or more number of players in it


```python
# Create a column with number of players by team in the dataframe
baseball >> group_by(X.Team_Name) >> summarize(player_count = n_distinct(X.Player_Name)) >> \
mask(X.player_count >= 7) 
# baseball %>% group_by(Team_Name) %>% summarise(player_count = n_distinct(X.Player_Name)) 
# %>% ungroup() %>% filter(player_count >= 7)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Team_Name</th>
      <th>player_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Angels</td>
      <td>8</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cardinals</td>
      <td>7</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Rangers</td>
      <td>7</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Tigers</td>
      <td>7</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Twins</td>
      <td>7</td>
    </tr>
    <tr>
      <th>28</th>
      <td>White Sox</td>
      <td>9</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Yankees</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>



### Its a must to pass a column name to n or n_distinct - Need to pass the granularity of the table to obtain frequency

## Compute the batting average, Batting Average = Team_total_hits/ Teams total at bat


```python
#Always remember to ungroup before performing any operations
baseball = baseball >> group_by(X.Team_Name) >> summarize(bat_avg = X.Hits.sum()/X.Bats.sum()) >> ungroup()
#baseball <- baseball %>% group_by(Team_Name) %>% summarize(bat_avg = sum(Hits)/sum(Bats)) %>% ungroup()

baseball >> head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Team_Name</th>
      <th>bat_avg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Angels</td>
      <td>0.287629</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Astros</td>
      <td>0.289931</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Athletics</td>
      <td>0.253380</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Blue Jays</td>
      <td>0.250563</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Braves</td>
      <td>0.266344</td>
    </tr>
  </tbody>
</table>
</div>



## Filter for teams with batting average greater than .2 and less than .25


```python
baseball >> mask(X.bat_avg >= 0.2,X.bat_avg <= 0.25)
# baseball %>% filter(bat_avg >= 0.2 & bat_avg <= 0.25)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Team_Name</th>
      <th>bat_avg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12</th>
      <td>Mariners</td>
      <td>0.242055</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Phillies</td>
      <td>0.250000</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Rays</td>
      <td>0.240749</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Reds</td>
      <td>0.249316</td>
    </tr>
  </tbody>
</table>
</div>



# Explore the spread, gather, unite and seperate functions


```python
student_score = pd.read_csv("C:/3-MSBA - Summer/Stat for Data Scientists/Stat Project/student-mat.csv")
student_score >> head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>sex</th>
      <th>age</th>
      <th>address</th>
      <th>famsize</th>
      <th>Pstatus</th>
      <th>Medu</th>
      <th>Fedu</th>
      <th>Medu_des</th>
      <th>Mjob</th>
      <th>...</th>
      <th>famrel</th>
      <th>freetime</th>
      <th>goout</th>
      <th>Dalc</th>
      <th>Walc</th>
      <th>health</th>
      <th>absences</th>
      <th>G1</th>
      <th>G2</th>
      <th>G3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GP</td>
      <td>F</td>
      <td>18</td>
      <td>U</td>
      <td>GT3</td>
      <td>A</td>
      <td>4</td>
      <td>4</td>
      <td>Higher</td>
      <td>at_home</td>
      <td>...</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>6</td>
      <td>5</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>GP</td>
      <td>F</td>
      <td>17</td>
      <td>U</td>
      <td>GT3</td>
      <td>T</td>
      <td>1</td>
      <td>1</td>
      <td>4th Grade</td>
      <td>at_home</td>
      <td>...</td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>GP</td>
      <td>F</td>
      <td>15</td>
      <td>U</td>
      <td>LE3</td>
      <td>T</td>
      <td>1</td>
      <td>1</td>
      <td>4th Grade</td>
      <td>at_home</td>
      <td>...</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>10</td>
      <td>7</td>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>GP</td>
      <td>F</td>
      <td>15</td>
      <td>U</td>
      <td>GT3</td>
      <td>T</td>
      <td>4</td>
      <td>2</td>
      <td>Higher</td>
      <td>health</td>
      <td>...</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>15</td>
      <td>14</td>
      <td>15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>GP</td>
      <td>F</td>
      <td>16</td>
      <td>U</td>
      <td>GT3</td>
      <td>T</td>
      <td>3</td>
      <td>3</td>
      <td>Secondary</td>
      <td>other</td>
      <td>...</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>5</td>
      <td>4</td>
      <td>6</td>
      <td>10</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 34 columns</p>
</div>



## Selecting columns using columns_to and columns_from


```python
student_score = student_score >> select(columns_to(2,inclusive = True),columns_from(-3))
# student_score %>% select(1:3,(length(names(student_score))-2):(length(names(student_score))))
student_score >> head(5)


```

## Roll up the data by school, sex and age


```python
student_score = student_score >> group_by(X.school,X.sex,X.age) >> summarize(G1_sum = X.G1.sum(), G2_sum = X.G2.sum() , G3_sum = X.G3.sum())
```

## Gather the dataset for the aggregated grade columns G1_sum,G2_sum and G3_sum


```python
student_score = student_score >> gather('variable','value',['G1_sum','G2_sum','G3_sum'])
#student_score %>% gather("variable","value",G1:G3)
```


```python
student_score >> head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>sex</th>
      <th>school</th>
      <th>variable</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>F</td>
      <td>GP</td>
      <td>G1_sum</td>
      <td>382</td>
    </tr>
    <tr>
      <th>1</th>
      <td>16</td>
      <td>F</td>
      <td>GP</td>
      <td>G1_sum</td>
      <td>551</td>
    </tr>
    <tr>
      <th>2</th>
      <td>17</td>
      <td>F</td>
      <td>GP</td>
      <td>G1_sum</td>
      <td>556</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18</td>
      <td>F</td>
      <td>GP</td>
      <td>G1_sum</td>
      <td>312</td>
    </tr>
    <tr>
      <th>4</th>
      <td>19</td>
      <td>F</td>
      <td>GP</td>
      <td>G1_sum</td>
      <td>135</td>
    </tr>
  </tbody>
</table>
</div>



## Spread the gathered columns


```python
student_score >> spread(X.variable,X.value) >> head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>sex</th>
      <th>school</th>
      <th>G1_sum</th>
      <th>G2_sum</th>
      <th>G3_sum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>F</td>
      <td>GP</td>
      <td>382</td>
      <td>372</td>
      <td>363</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15</td>
      <td>M</td>
      <td>GP</td>
      <td>539</td>
      <td>560</td>
      <td>560</td>
    </tr>
    <tr>
      <th>2</th>
      <td>16</td>
      <td>F</td>
      <td>GP</td>
      <td>551</td>
      <td>579</td>
      <td>569</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16</td>
      <td>M</td>
      <td>GP</td>
      <td>587</td>
      <td>584</td>
      <td>578</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17</td>
      <td>F</td>
      <td>GP</td>
      <td>556</td>
      <td>548</td>
      <td>531</td>
    </tr>
  </tbody>
</table>
</div>



## Unite function - combining the school and age columns


```python
student_score = student_score >> unite('school_age',X.school,X.age) 
# student_score <- student_score %>% unite(school_age,school,age,sep = '_')  
```

    ['school', 'age'] _ True maintain
    


```python
student_score >> head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sex</th>
      <th>variable</th>
      <th>value</th>
      <th>school_age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>G1_sum</td>
      <td>382</td>
      <td>GP_15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>G1_sum</td>
      <td>551</td>
      <td>GP_16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>G1_sum</td>
      <td>556</td>
      <td>GP_17</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>G1_sum</td>
      <td>312</td>
      <td>GP_18</td>
    </tr>
    <tr>
      <th>4</th>
      <td>F</td>
      <td>G1_sum</td>
      <td>135</td>
      <td>GP_19</td>
    </tr>
  </tbody>
</table>
</div>



## Separate function


```python
# You can also custom define the columns to assume NaN values based if the column consists unequal number of elements
student_score = student_score >> separate(X.school_age, ['school','age'],sep = "_",remove = True)
#student_score %>% separate(school_age, c('school','age'))
student_score >> head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sex</th>
      <th>variable</th>
      <th>value</th>
      <th>school</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>G1_sum</td>
      <td>382</td>
      <td>GP</td>
      <td>15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>G1_sum</td>
      <td>551</td>
      <td>GP</td>
      <td>16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>G1_sum</td>
      <td>556</td>
      <td>GP</td>
      <td>17</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>G1_sum</td>
      <td>312</td>
      <td>GP</td>
      <td>18</td>
    </tr>
    <tr>
      <th>4</th>
      <td>F</td>
      <td>G1_sum</td>
      <td>135</td>
      <td>GP</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
</div>


