{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# project on car evaluation using multiple classification algarithms"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1)we have many features in the data set containing the features like buying which says chance of buying that car is very high or high or low,in the same way there are many attrubutes we have to classify wheather it is accepted or not accepted and whether it is good or not."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>buying</th>\n",
       "      <th>maint</th>\n",
       "      <th>doors</th>\n",
       "      <th>persons</th>\n",
       "      <th>lug_boot</th>\n",
       "      <th>safety</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>small</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>small</td>\n",
       "      <td>med</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>small</td>\n",
       "      <td>high</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>med</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>med</td>\n",
       "      <td>med</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>med</td>\n",
       "      <td>high</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>big</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>big</td>\n",
       "      <td>med</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>big</td>\n",
       "      <td>high</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>small</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>small</td>\n",
       "      <td>med</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>small</td>\n",
       "      <td>high</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>med</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>med</td>\n",
       "      <td>med</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>med</td>\n",
       "      <td>high</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>big</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>big</td>\n",
       "      <td>med</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>big</td>\n",
       "      <td>high</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>more</td>\n",
       "      <td>small</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>more</td>\n",
       "      <td>small</td>\n",
       "      <td>med</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>more</td>\n",
       "      <td>small</td>\n",
       "      <td>high</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>more</td>\n",
       "      <td>med</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>more</td>\n",
       "      <td>med</td>\n",
       "      <td>med</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>more</td>\n",
       "      <td>med</td>\n",
       "      <td>high</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>more</td>\n",
       "      <td>big</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>more</td>\n",
       "      <td>big</td>\n",
       "      <td>med</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>2</td>\n",
       "      <td>more</td>\n",
       "      <td>big</td>\n",
       "      <td>high</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>small</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>small</td>\n",
       "      <td>med</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>vhigh</td>\n",
       "      <td>vhigh</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>small</td>\n",
       "      <td>high</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1698</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>4</td>\n",
       "      <td>more</td>\n",
       "      <td>big</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1699</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>4</td>\n",
       "      <td>more</td>\n",
       "      <td>big</td>\n",
       "      <td>med</td>\n",
       "      <td>good</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1700</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>4</td>\n",
       "      <td>more</td>\n",
       "      <td>big</td>\n",
       "      <td>high</td>\n",
       "      <td>vgood</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1701</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>2</td>\n",
       "      <td>small</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1702</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>2</td>\n",
       "      <td>small</td>\n",
       "      <td>med</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1703</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>2</td>\n",
       "      <td>small</td>\n",
       "      <td>high</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1704</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>2</td>\n",
       "      <td>med</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1705</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>2</td>\n",
       "      <td>med</td>\n",
       "      <td>med</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1706</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>2</td>\n",
       "      <td>med</td>\n",
       "      <td>high</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1707</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>2</td>\n",
       "      <td>big</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1708</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>2</td>\n",
       "      <td>big</td>\n",
       "      <td>med</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1709</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>2</td>\n",
       "      <td>big</td>\n",
       "      <td>high</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1710</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>4</td>\n",
       "      <td>small</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1711</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>4</td>\n",
       "      <td>small</td>\n",
       "      <td>med</td>\n",
       "      <td>acc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1712</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>4</td>\n",
       "      <td>small</td>\n",
       "      <td>high</td>\n",
       "      <td>good</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1713</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>4</td>\n",
       "      <td>med</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1714</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>4</td>\n",
       "      <td>med</td>\n",
       "      <td>med</td>\n",
       "      <td>good</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1715</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>4</td>\n",
       "      <td>med</td>\n",
       "      <td>high</td>\n",
       "      <td>vgood</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1716</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>4</td>\n",
       "      <td>big</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1717</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>4</td>\n",
       "      <td>big</td>\n",
       "      <td>med</td>\n",
       "      <td>good</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1718</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>4</td>\n",
       "      <td>big</td>\n",
       "      <td>high</td>\n",
       "      <td>vgood</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1719</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>more</td>\n",
       "      <td>small</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1720</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>more</td>\n",
       "      <td>small</td>\n",
       "      <td>med</td>\n",
       "      <td>acc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1721</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>more</td>\n",
       "      <td>small</td>\n",
       "      <td>high</td>\n",
       "      <td>good</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1722</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>more</td>\n",
       "      <td>med</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1723</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>more</td>\n",
       "      <td>med</td>\n",
       "      <td>med</td>\n",
       "      <td>good</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1724</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>more</td>\n",
       "      <td>med</td>\n",
       "      <td>high</td>\n",
       "      <td>vgood</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1725</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>more</td>\n",
       "      <td>big</td>\n",
       "      <td>low</td>\n",
       "      <td>unacc</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1726</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>more</td>\n",
       "      <td>big</td>\n",
       "      <td>med</td>\n",
       "      <td>good</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1727</th>\n",
       "      <td>low</td>\n",
       "      <td>low</td>\n",
       "      <td>5more</td>\n",
       "      <td>more</td>\n",
       "      <td>big</td>\n",
       "      <td>high</td>\n",
       "      <td>vgood</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1728 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     buying  maint  doors persons lug_boot safety  Class\n",
       "0     vhigh  vhigh      2       2    small    low  unacc\n",
       "1     vhigh  vhigh      2       2    small    med  unacc\n",
       "2     vhigh  vhigh      2       2    small   high  unacc\n",
       "3     vhigh  vhigh      2       2      med    low  unacc\n",
       "4     vhigh  vhigh      2       2      med    med  unacc\n",
       "5     vhigh  vhigh      2       2      med   high  unacc\n",
       "6     vhigh  vhigh      2       2      big    low  unacc\n",
       "7     vhigh  vhigh      2       2      big    med  unacc\n",
       "8     vhigh  vhigh      2       2      big   high  unacc\n",
       "9     vhigh  vhigh      2       4    small    low  unacc\n",
       "10    vhigh  vhigh      2       4    small    med  unacc\n",
       "11    vhigh  vhigh      2       4    small   high  unacc\n",
       "12    vhigh  vhigh      2       4      med    low  unacc\n",
       "13    vhigh  vhigh      2       4      med    med  unacc\n",
       "14    vhigh  vhigh      2       4      med   high  unacc\n",
       "15    vhigh  vhigh      2       4      big    low  unacc\n",
       "16    vhigh  vhigh      2       4      big    med  unacc\n",
       "17    vhigh  vhigh      2       4      big   high  unacc\n",
       "18    vhigh  vhigh      2    more    small    low  unacc\n",
       "19    vhigh  vhigh      2    more    small    med  unacc\n",
       "20    vhigh  vhigh      2    more    small   high  unacc\n",
       "21    vhigh  vhigh      2    more      med    low  unacc\n",
       "22    vhigh  vhigh      2    more      med    med  unacc\n",
       "23    vhigh  vhigh      2    more      med   high  unacc\n",
       "24    vhigh  vhigh      2    more      big    low  unacc\n",
       "25    vhigh  vhigh      2    more      big    med  unacc\n",
       "26    vhigh  vhigh      2    more      big   high  unacc\n",
       "27    vhigh  vhigh      3       2    small    low  unacc\n",
       "28    vhigh  vhigh      3       2    small    med  unacc\n",
       "29    vhigh  vhigh      3       2    small   high  unacc\n",
       "...     ...    ...    ...     ...      ...    ...    ...\n",
       "1698    low    low      4    more      big    low  unacc\n",
       "1699    low    low      4    more      big    med   good\n",
       "1700    low    low      4    more      big   high  vgood\n",
       "1701    low    low  5more       2    small    low  unacc\n",
       "1702    low    low  5more       2    small    med  unacc\n",
       "1703    low    low  5more       2    small   high  unacc\n",
       "1704    low    low  5more       2      med    low  unacc\n",
       "1705    low    low  5more       2      med    med  unacc\n",
       "1706    low    low  5more       2      med   high  unacc\n",
       "1707    low    low  5more       2      big    low  unacc\n",
       "1708    low    low  5more       2      big    med  unacc\n",
       "1709    low    low  5more       2      big   high  unacc\n",
       "1710    low    low  5more       4    small    low  unacc\n",
       "1711    low    low  5more       4    small    med    acc\n",
       "1712    low    low  5more       4    small   high   good\n",
       "1713    low    low  5more       4      med    low  unacc\n",
       "1714    low    low  5more       4      med    med   good\n",
       "1715    low    low  5more       4      med   high  vgood\n",
       "1716    low    low  5more       4      big    low  unacc\n",
       "1717    low    low  5more       4      big    med   good\n",
       "1718    low    low  5more       4      big   high  vgood\n",
       "1719    low    low  5more    more    small    low  unacc\n",
       "1720    low    low  5more    more    small    med    acc\n",
       "1721    low    low  5more    more    small   high   good\n",
       "1722    low    low  5more    more      med    low  unacc\n",
       "1723    low    low  5more    more      med    med   good\n",
       "1724    low    low  5more    more      med   high  vgood\n",
       "1725    low    low  5more    more      big    low  unacc\n",
       "1726    low    low  5more    more      big    med   good\n",
       "1727    low    low  5more    more      big   high  vgood\n",
       "\n",
       "[1728 rows x 7 columns]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "ds=pd.read_csv(\"car.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "by using all attributes we build a model to evaluate the car based on the details "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['vhigh' 'vhigh' '2' '2' 'small' 'low']\n",
      " ['vhigh' 'vhigh' '2' '2' 'small' 'med']\n",
      " ['vhigh' 'vhigh' '2' '2' 'small' 'high']\n",
      " ...\n",
      " ['low' 'low' '5more' 'more' 'big' 'low']\n",
      " ['low' 'low' '5more' 'more' 'big' 'med']\n",
      " ['low' 'low' '5more' 'more' 'big' 'high']]\n"
     ]
    }
   ],
   "source": [
    "x=ds.iloc[:,:-1].values\n",
    "y=ds.iloc[:,6:].values\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['unacc']\n",
      " ['unacc']\n",
      " ['unacc']\n",
      " ...\n",
      " ['unacc']\n",
      " ['good']\n",
      " ['vgood']]\n"
     ]
    }
   ],
   "source": [
    "print(y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we have to preprocess the data as the whole data is in categorical features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 3, 0, 0, 2, 1],\n",
       "       [3, 3, 0, 0, 2, 2],\n",
       "       [3, 3, 0, 0, 2, 0],\n",
       "       ...,\n",
       "       [1, 1, 3, 2, 0, 1],\n",
       "       [1, 1, 3, 2, 0, 2],\n",
       "       [1, 1, 3, 2, 0, 0]], dtype=object)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "l=LabelEncoder()\n",
    "x[:,0]=l.fit_transform(x[:,0])\n",
    "x[:,1]=l.fit_transform(x[:,1])\n",
    "x[:,2]=l.fit_transform(x[:,2])\n",
    "x[:,3]=l.fit_transform(x[:,3])\n",
    "x[:,4]=l.fit_transform(x[:,4])\n",
    "x[:,5]=l.fit_transform(x[:,5])\n",
    "x\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 2, 2, ..., 2, 1, 3], dtype=int64)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y=l.fit_transform(y)\n",
    "y"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# splitting the data into training and testing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 0, 1, 0, 0, 2],\n",
       "       [2, 0, 2, 0, 2, 1],\n",
       "       [0, 3, 3, 2, 0, 1],\n",
       "       ...,\n",
       "       [2, 2, 0, 1, 0, 2],\n",
       "       [3, 2, 0, 2, 2, 2],\n",
       "       [2, 0, 3, 0, 0, 0]], dtype=object)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=1)\n",
    "x_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 2, 2, ..., 0, 2, 2], dtype=int64)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[2, 1, 1, 2, 2, 1],\n",
       "       [0, 0, 1, 2, 0, 2],\n",
       "       [0, 0, 3, 0, 1, 2],\n",
       "       ...,\n",
       "       [1, 3, 2, 2, 1, 0],\n",
       "       [2, 2, 2, 2, 0, 2],\n",
       "       [3, 3, 2, 0, 2, 0]], dtype=object)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 0, 2, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2,\n",
       "       2, 2, 2, 2, 2, 2, 2, 0, 3, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2,\n",
       "       2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 1, 2, 2,\n",
       "       2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 0, 0, 0, 0, 0, 1, 2, 2, 3, 0, 2,\n",
       "       0, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 0, 2, 2, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 2, 3, 2, 2, 3, 2, 2, 2, 2, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2,\n",
       "       1, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0, 2, 2, 3, 2, 2, 0, 2,\n",
       "       2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 3, 0, 0, 2, 0, 2, 3, 2, 2, 2, 2,\n",
       "       2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 1, 0, 2, 2, 0, 2, 2, 2,\n",
       "       0, 1, 2, 0, 2, 0, 2, 2, 2, 2, 1, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0,\n",
       "       2, 2, 2, 1, 2, 2, 2, 0, 1, 2, 2, 2, 0, 2, 2, 1, 2, 2, 2, 2, 2, 2,\n",
       "       2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2,\n",
       "       2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 0, 2, 0, 0, 2, 2,\n",
       "       0, 1, 2, 2, 2, 2, 0, 2, 2, 0, 0, 2, 3, 2, 2, 2, 1, 0, 2, 2, 2, 2,\n",
       "       2, 0, 2, 2, 2, 0, 2, 0, 0, 2, 2, 0, 2, 2, 2, 0, 0, 2, 2, 0, 2, 2,\n",
       "       0, 0, 0, 2, 1, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 2, 0, 2, 2, 2, 2,\n",
       "       2, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 1, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2,\n",
       "       3, 3, 3, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 2], dtype=int64)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# applying decison tree algarithm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 0, 2, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2,\n",
       "       2, 2, 2, 2, 2, 2, 2, 0, 3, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2,\n",
       "       2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 3, 2, 1, 2, 2,\n",
       "       2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 0, 1, 0, 0, 0, 1, 2, 2, 3, 0, 2,\n",
       "       0, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 0, 2, 2, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 2, 3, 2, 2, 3, 2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2,\n",
       "       1, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0, 2, 2, 3, 2, 2, 0, 2,\n",
       "       2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 3, 0, 0, 2, 0, 2, 3, 2, 2, 2, 2,\n",
       "       2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 1, 0, 2, 2, 0, 2, 2, 2,\n",
       "       0, 1, 2, 0, 2, 0, 2, 2, 2, 0, 1, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0,\n",
       "       2, 2, 2, 2, 2, 2, 2, 0, 1, 2, 2, 2, 0, 2, 2, 1, 2, 2, 2, 2, 2, 0,\n",
       "       2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 0, 2, 2, 0, 0, 2,\n",
       "       2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 0, 2, 0, 0, 2, 2,\n",
       "       0, 1, 2, 2, 2, 2, 0, 2, 2, 0, 0, 2, 3, 2, 2, 2, 1, 0, 2, 2, 2, 2,\n",
       "       2, 0, 2, 2, 2, 0, 2, 0, 0, 2, 2, 0, 2, 2, 2, 0, 0, 2, 2, 0, 2, 2,\n",
       "       0, 0, 0, 2, 1, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 2, 0, 2, 2, 2, 2,\n",
       "       2, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 1, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2,\n",
       "       3, 3, 3, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 2], dtype=int64)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "dt=DecisionTreeClassifier(criterion='entropy',random_state=0)\n",
    "dt.fit(x_train,y_train)\n",
    "d_pred=dt.predict(x_test)\n",
    "d_pred"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# confusion matrix for decision tree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 87,   1,   0,   0],\n",
       "       [  0,  17,   1,   0],\n",
       "       [  6,   0, 304,   0],\n",
       "       [  0,   0,   0,  16]], dtype=int64)"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "a11=confusion_matrix(y_test,d_pred)\n",
    "a11"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# applying random forest classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 0, 2, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2,\n",
       "       2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2,\n",
       "       2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 3, 2, 1, 2, 2,\n",
       "       2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 0, 1, 0, 0, 0, 1, 2, 2, 3, 0, 2,\n",
       "       0, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 0, 2, 2, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 0, 3, 2, 2, 3, 2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2,\n",
       "       1, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 0, 2,\n",
       "       2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 3, 0, 0, 2, 0, 2, 3, 2, 2, 2, 2,\n",
       "       2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 1, 0, 2, 2, 0, 2, 2, 2,\n",
       "       0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 1, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 0,\n",
       "       2, 2, 2, 0, 2, 0, 2, 0, 1, 2, 2, 2, 0, 2, 2, 1, 2, 2, 2, 2, 2, 0,\n",
       "       2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2,\n",
       "       2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 2, 2, 0, 0, 2, 2,\n",
       "       0, 1, 2, 2, 2, 2, 0, 2, 2, 0, 0, 2, 3, 2, 2, 2, 0, 0, 2, 2, 2, 2,\n",
       "       2, 0, 2, 2, 2, 0, 2, 0, 0, 2, 2, 0, 2, 2, 2, 0, 0, 2, 2, 0, 2, 2,\n",
       "       0, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 0, 2, 2, 2, 2,\n",
       "       2, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2,\n",
       "       3, 3, 3, 2, 2, 2, 2, 2, 1, 2, 0, 0, 0, 2], dtype=int64)"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "rf=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)\n",
    "rf.fit(x_train,y_train)\n",
    "r_pred = rf.predict(x_test)\n",
    "r_pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 82,   1,   5,   0],\n",
       "       [  4,  14,   0,   0],\n",
       "       [  7,   0, 303,   0],\n",
       "       [  1,   0,   0,  15]], dtype=int64)"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "a11=confusion_matrix(y_test,r_pred)\n",
    "a11"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# applying naive bayes classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 3, 3, 2, 2, 3, 2, 2, 3,\n",
       "       2, 2, 2, 3, 3, 2, 2, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2,\n",
       "       3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 3, 2,\n",
       "       2, 3, 3, 2, 2, 2, 2, 2, 0, 2, 2, 3, 3, 2, 2, 2, 3, 2, 2, 3, 3, 3,\n",
       "       3, 2, 3, 2, 2, 2, 2, 3, 2, 3, 2, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 3,\n",
       "       2, 2, 2, 2, 3, 2, 2, 0, 3, 2, 2, 2, 3, 3, 3, 2, 2, 2, 3, 2, 2, 2,\n",
       "       2, 3, 3, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 2, 3, 2, 2, 2, 2, 2, 2,\n",
       "       2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3,\n",
       "       3, 2, 2, 2, 2, 2, 3, 3, 2, 0, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 2, 2,\n",
       "       2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2,\n",
       "       2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 3, 2, 3, 2, 3, 3, 2, 2, 0, 2, 2, 2,\n",
       "       0, 2, 2, 2, 2, 2, 3, 2, 3, 3, 2, 2, 2, 2, 0, 2, 3, 2, 2, 2, 2, 3,\n",
       "       2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 2, 2, 2, 3,\n",
       "       2, 2, 3, 2, 0, 2, 2, 2, 2, 2, 2, 3, 2, 3, 3, 2, 2, 2, 2, 3, 2, 2,\n",
       "       2, 2, 2, 2, 3, 2, 2, 3, 3, 2, 2, 2, 2, 2, 3, 3, 2, 3, 2, 0, 2, 2,\n",
       "       2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 3, 2, 2,\n",
       "       2, 2, 2, 2, 3, 3, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 3, 2, 2, 3, 3, 3,\n",
       "       2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 2, 2, 2, 2,\n",
       "       2, 2, 2, 3, 2, 3, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 3, 2,\n",
       "       3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 0, 2], dtype=int64)"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.naive_bayes import GaussianNB \n",
    "gnb = GaussianNB() \n",
    "gnb.fit(x_train, y_train)\n",
    "g_pred=gnb.predict(x_test)\n",
    "g_pred"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# confusion matrix for nb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 10,   0,  39,  39],\n",
       "       [  3,   0,   8,   7],\n",
       "       [  2,   0, 261,  47],\n",
       "       [  0,   0,   0,  16]], dtype=int64)"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "a11=confusion_matrix(y_test,g_pred)\n",
    "a11"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# evaluating the model by combining all three models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 0, 2, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2,\n",
       "       2, 2, 2, 2, 2, 2, 2, 0, 3, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2,\n",
       "       2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 3, 2, 1, 2, 2,\n",
       "       2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 0, 1, 0, 0, 0, 1, 2, 2, 3, 0, 2,\n",
       "       0, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 0, 2, 2, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 0, 3, 2, 2, 3, 2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2,\n",
       "       1, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 0, 2,\n",
       "       2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 3, 0, 0, 2, 0, 2, 3, 2, 2, 2, 2,\n",
       "       2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 1, 0, 2, 2, 0, 2, 2, 2,\n",
       "       0, 0, 2, 0, 2, 0, 2, 2, 2, 0, 1, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0,\n",
       "       2, 2, 2, 0, 2, 2, 2, 0, 1, 2, 2, 2, 0, 2, 2, 1, 2, 2, 2, 2, 2, 0,\n",
       "       2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2,\n",
       "       2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 2, 2, 0, 0, 2, 2,\n",
       "       0, 1, 2, 2, 2, 2, 0, 2, 2, 0, 0, 2, 3, 2, 2, 2, 0, 0, 2, 2, 2, 2,\n",
       "       2, 0, 2, 2, 2, 0, 2, 0, 0, 2, 2, 0, 2, 2, 2, 0, 0, 2, 2, 0, 2, 2,\n",
       "       0, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 0, 2, 2, 2, 2,\n",
       "       2, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2,\n",
       "       3, 3, 3, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 2])"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b1=[]\n",
    "for i in range(len(x_test)):\n",
    "    fi,se,th,fo=0,0,0,0\n",
    "    if(d_pred[i]==0):\n",
    "        fi=fi+1\n",
    "    if(r_pred[i]==0):\n",
    "        fi=fi+1\n",
    "    if(g_pred[i]==0):\n",
    "        fi=fi+1\n",
    "    if(d_pred[i]==1):\n",
    "        se=se+1\n",
    "    if(r_pred[i]==1):\n",
    "        se=se+1\n",
    "    if(g_pred[i]==1):\n",
    "        se=se+1\n",
    "    if(d_pred[i]==2):\n",
    "        th=th+1\n",
    "    if(r_pred[i]==2):\n",
    "        th=th+1\n",
    "    if(g_pred[i]==2):\n",
    "        th=th+1\n",
    "    if(d_pred[i]==3):\n",
    "        fo=fo+1\n",
    "    if(r_pred[i]==3):\n",
    "        fo=fo+1\n",
    "    if(g_pred[i]==3):\n",
    "        fo=fo+1\n",
    "    if(max(fi,se,th,fo)==fi):\n",
    "        b1.append(0)\n",
    "    elif(max(fi,se,th,fo)==se):\n",
    "        b1.append(1)\n",
    "    elif(max(fi,se,th,fo)==th):\n",
    "        b1.append(2)\n",
    "    elif(max(fi,se,th,fo)==fo):\n",
    "        b1.append(3)\n",
    "b=np.array(b1)\n",
    "b"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# confusion matrix of combined models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 84,   1,   3,   0],\n",
       "       [  4,  14,   0,   0],\n",
       "       [  6,   0, 304,   0],\n",
       "       [  0,   0,   0,  16]], dtype=int64)"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "org=confusion_matrix(y_test,b)\n",
    "org"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "96.75925925925925"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum1=org[0][0]+org[1][1]+org[2][2]+org[3][3]\n",
    "accuracy=sum1/sum(sum(org))\n",
    "accuracy*100"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "i achieved 96.7% of accuracy by combining all the models finally i conclude i have used three models to evaluate a car and achieved 96.7% of accuracy in my model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
