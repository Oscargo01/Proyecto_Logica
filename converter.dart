import 'package:flutter/material.dart';

class Converter extends StatefulWidget {
  @override
  _ConverterState createState() => _ConverterState();
}

class _ConverterState extends State<Converter> {
  String _binary = "";
  String _decimal = "0"; // _decimal = int.parse(_binary, radix: 2).toRadixString(10);

  void _onPressed(int n) {
    setState(() {
      if(n == 0){
      _binary += "0";
    }else{
      _binary += "1";
    }
    _decimal = int.parse(_binary, radix: 2).toRadixString(10);
    });
    
  }

  @override
  Widget build(BuildContext context) {
    var height2 = 100000;
    return Container(
     child: 
     
        Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: <Widget>[
            Container(
               alignment: Alignment.centerLeft,
              child: Text("Binary -> Decimal")
              ),
        Container(
              padding: const EdgeInsets.all(8.0),
              alignment: Alignment.centerRight,
              child: Text(
                '$_binary',
                textAlign: TextAlign.right,
                style: TextStyle(
                    fontWeight: FontWeight.bold,
                    color: Color(int.parse("#FF5722".replaceAll('#', '0xff'))),
                    fontSize: 35),
              )),
            Container(
              padding: const EdgeInsets.all(8.0),
              alignment: Alignment.centerRight,
              child: Text(
                '$_decimal',
                textAlign: TextAlign.right,
                style: TextStyle(
                    fontWeight: FontWeight.bold,
                    color: Color(int.parse("#FF5722".replaceAll('#', '0xff'))),
                    fontSize: 35),
              )),
            Flexible(flex: 3,child:Row(crossAxisAlignment: CrossAxisAlignment.stretch,
                children: <Widget>[
                  Expanded(flex: 1,
                  child:MaterialButton(
                   color: Color(int.parse("#0069C0".replaceAll('#', '0xff'))),
                  onPressed: () {_onPressed(1);
                   
                  },
                  child: Text("1",
                      style: new TextStyle(
                        fontSize: 20.0,
                        color: Colors.white,
                      )),
                  ) ,)
                  ,
                  Spacer(),
                  Expanded(flex: 1,
                  child:MaterialButton(
                    color: Color(int.parse("#0069C0".replaceAll('#', '0xff'))),
                  onPressed: () { _onPressed(0);
                   
                  },
                  child: Text("0",
                      style: new TextStyle(
                        fontSize: 20.0,
                        color: Colors.white,
                      )),
                  ) ,)
                  ,
                ]) ,)
            ,

          Flexible(
            flex: 1,
            fit: FlexFit.tight,
            child: Container(
              padding: const EdgeInsets.all(8.0),
              child: MaterialButton(
                  
                  color: Color(int.parse("#0069C0".replaceAll('#', '0xff'))),
                  onPressed: () {
                    setState(() {
                      _binary = ""; _decimal = "0";
                    }); 
                   
                  },
                  child: Text("Reset",
                      style: new TextStyle(
                        fontSize: 20.0,
                        color: Colors.white,
                      ))),
            ),
          ),
          ]),


    );
  }
}
