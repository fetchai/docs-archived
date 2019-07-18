In order to implement a static contract, create a new class that inherits from the `Contract` class and expose the relevant functions. 

In the following example, we will describe an implementation of the the Fetch token. 

First, we define the body of the contract as below:


``` c++
class TokenContract : public Contract
{
public:
  TokenContract();
  ~TokenContract() = default;

  static constexpr char const *LOGGING_NAME = "TokenContract";

private:
  // transaction handlers
  Status CreateWealth(Transaction const &tx);
  Status Transfer(Transaction const &tx);

  // queries
  Status Balance(Query const &query, Query &response);
};

```