# Persian-ATIS (Airline Travel Information System) Dataset
We present the first publicly available benchmark in the Persian language for intent detection and slot filling. We investigate the state-of-the-art models for intent detection and slot filling to apply them to our recently founded benchmark and explain how they perform on this particular dataset. Our goal is to provide valuable training data as well as a novel and demanding testing ground for NLU models.

---
An example of supplants of words after translation and the need to
relabel slot tags:
<p align="center">
<img src="https://github.com/Makbari1997/Persian-Atis/blob/main/figure.png"  width="50%"  height="30%">
</p>
---



### Download Dataset
There are Persian and English datasets available with splits and loading code.

| dataset name | language   | train | dev   | test  |         
| :----------- | :--------: | :---: | :---: | :---: | 
| ATIS         | `en`       | ✔     | ✔    | ✔     | 
| PATIS        | `fa`       | ✔     | ✔    | ✔     |

### Results
**Intent accuracy** percent of state-of-the-art models on English and Persian ATIS dataset

| Taxonomy | Model  | English | Persian   |        
| :----------- | :--------: | :---: | :---: |
| Single         |CNN-LSTM-CRF       | 93.62    |89.70   | 
| Joint        |CNN-LSTM-CRF      | 93.73     | 91.83    | 
| Joint        |Attention RNN     | 93.84    | 90.93    | 
| Joint        |Slot-Gated     |94.62    | 94.62    | 
| Joint        |SF-ID,SF-first  |96.65     | 92.38    | 
| Joint        | SF-ID+CRF,SF-first      |97.31   | 97.31   | 
| Joint        |SF-ID,ID-first      |97.09    | 97.09 | 
| Joint        |SF-ID+CRF,ID-first    |95.41    | 92.05   | 
| Joint        | Co-Interactive transformer (Glove)  | **97.54** | 91.83    | 
| Pre-trained        |JointBERT     | 97.42    | **97.65**    | 


**Slot F1-Score** of sate-of-the-art models on English and Persian ATIS dataset
| Taxonomy | Model  | English | Persian   |        
| :----------- | :--------: | :---: | :---: |
| Single         |CNN-LSTM-CRF       |94.46    |88.41   | 
| Joint        |CNN-LSTM-CRF      |85.31     |81.68    | 
| Joint        |Attention RNN     |95.59   |87.96    | 
| Joint        |Slot-Gated     |94.91    |87.70   | 
| Joint        |SF-ID,SF-first  |94.65   | 85.38    | 
| Joint        | SF-ID+CRF,SF-first      |94.72 | 85.56   | 
| Joint        |SF-ID,ID-first      |95.06   |85.32| 
| Joint        |SF-ID+CRF,ID-first    |94.55   | 85.57   | 
| Joint        | Co-Interactive transformer (Glove)  | **95.69** | 86.14    | 
| Pre-trained        |JointBERT     |95.20   | **96.75**    | 

### Credit
* English dataset derived from [ATIS DataSet by siddhadev](https://www.kaggle.com/siddhadev/atis-dataset)

---
### Citing & Authors

Our dataset for joint intent detection and slot filling in Persian language was created at the **[Natural Language Processing Innovation Center (NLPIC)](https://nlpic.aut.ac.ir/)** at **Amirkabir University of Technology** with the collaboration of all the members of the lab. The team at NLPIC worked hard to extend the original ATIS dataset to create a comprehensive and publicly available benchmark for the Persian language. We are proud of the efforts of all the members of the lab who contributed to the development of this benchmark.

To acknowledge the contribution of our lab members, we have included a citation on our GitHub page, where the dataset is publicly available. This citation recognizes the work of our lab and highlights the importance of collaboration in achieving our research goals. We believe that this citation will help to increase the visibility of our dataset and encourage others in the NLP community to use and build upon our work.
[A Persian Benchmark for Joint Intent Detection and Slot Filling](https://arxiv.org/abs/2303.00408):

```bibtex 
@misc{2303.00408,
Author = {Masoud Akbari and Amir Hossein Karimi and Tayyebeh Saeedi and Zeinab Saeidi and Kiana Ghezelbash and Fatemeh Shamsezat and Mohammad Akbari and Ali Mohades},
Title = {A Persian Benchmark for Joint Intent Detection and Slot Filling},
Year = {2023},
Eprint = {arXiv:2303.00408},
}
```
