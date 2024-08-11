import json

def lambda_handler(event, context):
    try:
        # Extract numbers and operation from the event
        num1 = float(event['queryStringParameters']['num1'])
        num2 = float(event['queryStringParameters']['num2'])
        operation = event['queryStringParameters']['operation']
        
        # Perform calculation based on the operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                raise ValueError('Division by zero is not allowed.')
            result = num1 / num2
        else:
            raise ValueError('Invalid operation.')

        # Return result as JSON
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
