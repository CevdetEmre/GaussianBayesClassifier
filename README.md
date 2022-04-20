# GaussianBayesClassifier

When working with continuous data, one common assumption is that the continuous values associated with each class follow a normal (or Gaussian) distribution. The characteristics' probability is considered to be-


![image](https://user-images.githubusercontent.com/86251983/164312046-7de75b56-b0f3-4980-92ba-2a8d127ffd3a.png)

Sometimes assume variance

is independent of Y (i.e., σi),
or independent of Xi (i.e., σk)
or both (i.e., σ)

Gaussian Naive Bayes accepts continuous valued features and models them all as Gaussian (normal) distributions.

To build a basic model, assume the data is characterized by a Gaussian distribution with no covariance (independent dimensions) between the parameters. This model may be fitted by simply calculating the mean and standard deviation of the points within each label, which is all that is required to construct a distribution of this type.

![image](https://user-images.githubusercontent.com/86251983/164312173-18d81482-9d3b-475b-b976-09350a9d4911.png)

A Gaussian Naive Bayes (GNB) classifier is depicted in the diagram above. The z-score distance between each data point and each class mean is determined, which is the distance from the class mean divided by the class standard deviation.

As a result, we can observe that the Gaussian Naive Bayes technique is slightly different and may be employed well.
