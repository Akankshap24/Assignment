function Transactions(balance, transaction_type, transactionAmount){
    let trans_type=['UPI','Card','Cheque'];
    if(balance<transactionAmount){
        console.log("Transaction Failed");
    }else{
       switch (transaction_type){
        case 'UPI':
            if(transactionAmount<=4000) 
                console.log("Transaction Successful", balance-transactionAmount);
            else 
                console.log("Transaction Failed");
            break;
         case 'Card':
            if(transactionAmount<=10000) 
                console.log("Transaction Successful", balance-transactionAmount);
            else 
                console.log("Transaction Failed");
            break;
         case 'Cheque':
            if(transactionAmount<=100000) 
                console.log("Transaction Successful", balance-transactionAmount);
            else 
                console.log("Transaction Failed");
            break;
         default:
            console.log("Invalid transaction ");
            break;
       }
    }  
}

Transactions(10000,'Card',7000); 
