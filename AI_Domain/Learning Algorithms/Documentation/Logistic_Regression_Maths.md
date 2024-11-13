# Theory for Logistic Regression

We could approach the classification problem ignoring the fact that $y$ is discrete-valued, and use our old linear regression algorithm to try to predict $y$ given $x$. However, it is easy to construct examples where this method performs very poorly. Intuitively, it also doesn’t make sense for $h_{\theta}(x)$ to take values larger than 1 or smaller than 0 when we know that $y \in \{0, 1\}$.  

To fix this, let’s change the form for our hypotheses $h_{\theta}(x)$. We will choose:
$$ h_{\theta}(x) = g(\theta^T x) = \frac{1}{1 + e^{-\theta^T x}} $$

In this equation, $g(z)$ is called the logistic function or the sigmoid function. It can be written as: 
$$ g(z) = \frac{1}{1 + e^{-z}} $$

If we plot the sigmoid function on a graph, it looks as follows:  
![s16184211132024](https://a.okmd.dev/md/6734840a9cf7c.png)

Now, let us assume that: 
$$ P(y = 1 \mid x; \theta) = h_{\theta}(x) $$

$$ P(y = 0 \mid x; \theta) = 1 - h_{\theta}(x) $$

Assuming that the $n$ training examples were generated independently, we can then write down the likelihood of the parameters as:
$$ L(\theta) = \prod_{i=1}^{n} \left[ h_{\theta}(x^{(i)})^{y^{(i)}} \left( 1 - h_{\theta}(x^{(i)}) \right)^{1 - y^{(i)}} \right] $$

Since it is easier to maximize the log likelihood:
$$ \log L(\theta) = \sum_{i=1}^{n} \left[ y^{(i)} \log h_{\theta}(x^{(i)}) + (1 - y^{(i)}) \log(1 - h_{\theta}(x^{(i)})) \right] $$

To maximize the log-likelihood function and find the optimal values for the parameters $ \theta $, we use Gradient Ascent. The update rule for each parameter $ \theta_j $ is:

$$ \theta_j := \theta_j + \sum_{i=1}^{m} \frac{\partial \log L(\theta)}{\partial \theta_j} $$

By substituting the value of $ \ell(\theta) $ from above and solving the derivatives, we get:

$$ \theta_j := \theta_j + \alpha \sum_{i=1}^{m} \left( y^{(i)} - h_{\theta}(x^{(i)}) \right) x_j^{(i)} $$

