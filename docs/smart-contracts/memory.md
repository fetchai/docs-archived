<h1>Memory</h1> 

`State` and `ShardedState` store data on the shards that make up the ledger. There are a configurable number of parallel shards on the ledger that accept permanent, irreversible storage. 

Developers have to pay to store data on ledger shards so they should take care when constructing `State` and `ShardedState` types to avoid unnecessary fees. 

Ensuring that smart contract data is evenly spread across ledger shards is the most efficient and economical way to code and execute smart contracts in `etch`.

The trick is to ensure that `etch` code avoids taking up too much memory on a single shard or taking up too much memory on too many shards as more memory costs more to deploy.

It is possible to exceed `etch` imposed limits on data storage in which case an `etch` smart contract will fail. 

## Design considerations

You can visualise the ledger shards as a series of swim lanes. 

Data etches onto a shard depending on the smart contract design. The contents of a `State` etch onto a single shard on the ledger. 

For example, 

``` c++
function main()

    var myState1 = State<Int32>("balance");
    myState1.set(200);

endfunction
``` 

The above integer value may etch onto a shard like this:

<center>![Memory mapping on the Fetch.AI ledger shards](img/shards.png)</center>

This is an economical way to manage memory on the ledger shards. However, there are scenarios in which `State` data etches onto the ledger in an inefficient way. 

Aggregate functions may store too much data on too many shards on the ledger if coded inappropriately. Code like this can block other users and slow the network. Data fees will reflect this. 

For example, given a `vote()` function such as the one below, the code may aggregate the vote tracking `State` variables in an inefficient manner.

``` c++

function main()

    vote();

endfunction

function vote()

    // declare and set politics account
    
    var race_for_prime_minister = "hustings";

    var votes_for = State<Int32>(race_for_prime_minister);
    votes_for.set(0);
    var votes_against = State<Int32>(race_for_prime_minister);
    votes_against.set(0);
    var votes_total = State<Int32>(race_for_prime_minister);
    votes_total.set(0);
    var votes_sum = State<Int32>(race_for_prime_minister);
    votes_sum.set(0);

    // ..and further along..

    if (true)
        // update the aggregate votes for
        votes_for.set(votes_for.get() + 1);
    else 
        // update the aggregate votes against
        votes_against.set(votes_against.get() + 1);
    endif
    
    // update the aggregate of total votes
    votes_sum.set(votes_total.get() + 1);

endfunction

```

Each time a `State` increments, the new data value takes up a new memory space on the shard.

The ledger shards could look something like this after the `vote()` function runs over a short period of time.

<center>![Bad memory mapping on the Fetch.AI ledger shards](img/bad-sharding.png)</center>

This is highly uneconomical. Every aggregate value for a single `State` takes up its own spot on a ledger shard. Furthermore, multiple `States` take up multiple shards. 

Data is chargeable per lane in order to disincentivise code like the above which can slow the network. 

There are better approaches to the voting problem. For example, by encapsulating the data with a `ShardedState` and performing calculations in functions outside the ledger.


``` c++
function main()

  vote();

endfunction

function vote()

    var fors = ShardedState<Int32>("votes_for");
    fors.set("Alice", increment(fors.get("Alice", 0)));
    // etc.

endfunction

function increment(x : Int32) : Int32
    
    var y = x + 1;
    return y;

endfunction

```


<br/>