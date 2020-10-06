import boto3


def main():
    print("Available instances")
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.all()
    instanceNames = []
    for instance in instances:
        for tags in instance.tags:
            if tags["Key"] == 'Name':
                instanceName = tags["Value"]
                instanceNames.append(instanceName)
        print(instance.id + " Instance Tag: " + instanceName)
    instanceTag = input("Enter the instance name: ")
    print("Checking for " + instanceTag)
    if instanceTag not in instanceNames:
        print("invalid tag name")
    else:
        print("Instance found...")
        status = input("Start or Stop: ")
        if status == "Start":
            filters = [{'Name': 'tag:Name', 'Values': [instanceTag]}]
            selectedInstance = ec2.instances.filter(Filters=filters).start()
            print(selectedInstance)
        elif status == "Stop":
            filters = [{'Name': 'tag:Name', 'Values': [instanceTag]}]
            selectedInstance = ec2.instances.filter(Filters=filters).stop()
            print(selectedInstance)
        else:
            print("invalid input")


if __name__ == '__main__':
    main()
