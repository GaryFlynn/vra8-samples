exports.handler = function handler(context, inputs) {
  let greeting = "Hello, " +  inputs.target + "!" ;
  console.log(greeting);

  let outputs = {
    "greeting": greeting
  };

  return outputs;
};
