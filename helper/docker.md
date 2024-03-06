# What is Docker & Docker Container?
<br>

`ডকার হল একধরনের লিনাক্স **কন্টেইনার** টেকনোলজি । এর কাজ হল ডেভেলপমেন্ট এর জন্য আপনার অ্যাপ্লিকেশান লেয়ার কে সিস্টেম লেয়ার থেকে আলাদা করা । এটা একটা Cross Platform টুল যেটা উইন্ডোজ , লিনাক্স , ম্যাক , পাওয়ার পিসি সহ অনেক অনেক অপারেটিং সিস্টেম এ চলে ।`

<br>

- Container কিভাবে কাজ করে?
কার্গো জাহাজে যেভাবে কন্টেইনার সাজানো হয়, যেখানে একটির সাথে আরেকটির কোনো সম্পর্ক থাকে না। ঠিক একই ভাবে কন্টেইনার ইঞ্জিনের (Like Docker) উপরে বিভিন্ন কন্টেইনার ভিত্তিক অ্যাপ্লিকেশন রান করানো হয়। একটি কন্টেইনার প্ল্যাটফর্মের (Like Docker) উপরে অনেকগুলা কন্টেইনার তৈরি করা যায় এবং এক একটি কন্টেইনার আলাদা সার্ভিস/অ্যাপ্লিকেশন হিসেবে ব্যবহার করা যায়। কন্টেইনার টেকনোলজি প্রসেস লেভ'isolation' করে ফলে, এক কন্টেইনারের প্রেসেসের সাথে আরেক কন্টেইনারের প্রেসেস অথবা কন্টেইনার প্রসেসের সাথে হোস্ট (Host) সিস্টেমের প্রসেসের মধ্যে কোনো সম্পর্ক থাকে না।  প্রতিটি কন্টেইনার সরাসরি অপারেটিং সিস্টেম (OS) হতে প্রয়োজনীয় রিসোর্স (Kernel, Memory, Storage, Network, etc.) ব্যবহার করে।এক একটি কন্টেইনার ইমেজ মূলত নির্দিষ্ট অ্যাপ্লিকেশন/সার্ভিসের (Like Apache, mySQL, nginx) জন্য ব্যবহার করা হয় এবং এক একটি কন্টেইনার একটি পূর্ণাঙ্গ (Complete) প্যাকেজ, যার মধ্যে শুধুমাত্র নির্দিষ্ট অ্যাপ্লিকেশনের জন্য প্রয়োজনীয় কোড, বাইনারী (Binaries), সিস্টেম লাইব্রেরী (Libraries) থাকে। ফলে, এটার সাইজ খুবই ছোট (MBs) হয় এবং ভার্চুয়াল মেশিন (VM) থেকে অনেক দ্রুত রান করে এবং কাজ করে। 
<br>

# devops এর সাথে docker: 
- DevOps হল একটি software development methodology যা software development থেকে “Dev” শব্দ এবং IT operations থেকে “Ops” শব্দ দুটির মিশ্রিত একটি নাম। যার অর্থ দাঁড়ায় DevOps হচ্ছে কিছু practice, tools, process গুলো এবং এমনকি কোম্পানির লোকেদের একটি সেট যা একটি দলের মধ্যে আরও বেশি সহযোগিতা এবং দ্রুত, আরও নির্ভরযোগ্য product release এর উদ্দেশ্য রাখে।<br>
![Alt text](/helper/images/image.png)


for more about [devops](https://github.com/yasin-arafat-05/rest_api_fastapi/blob/main/helper/devops.md)


<br> <br> <br>

# Create Docker for fastapi: 

- first, create requirement.txt file with a single command: ```pip freeze > requirement.txt```
- then, create a file name `Dockerfile` and follow the steps below:
    - **Choose a Base Image:** Start by choosing a base image that includes the necessary Python runtime and libraries. For FastAPI, using an image with a Python runtime is common. Here's an example using the `python:3.9` image as a base:
    <br>

    ```Dockerfile
    FROM python:3.9
    ```
    <br>

    - **Set the Working Directory:**
    Set the working directory inside the container where your application code will be placed.
    <br>

    ```Dockerfile
    WORKDIR /app
    ```
    <br>
    
    - **Copy the Application Files:** Copy your FastAPI application files (Python scripts, requirements.txt, etc.) into the container.

    <br>

   ```Dockerfile
   COPY . /app
   ```
    <br>

    -  **Install Dependencies:** Install the required dependencies using `pip`. This step involves copying the `requirements.txt` file into the container and running `pip install`.

    <br>

   ```Dockerfile
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   ```

    <br>

    - **Expose the Port:**
   Expose the port that your FastAPI application will run on.
    <br>

   ```Dockerfile
   EXPOSE 8000
   ```
    <br>

    - **Command to Run the Application:**
   Specify the command to run your FastAPI application. Typically, you'll use `uvicorn` to run the FastAPI app.
    <br>

   ```Dockerfile
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```
    <br>

   Make sure to adjust the `"main:app"` part based on your project structure.
    <br>

    - **Build and Run the Docker Image:**
   Build the Docker image using the following command:
    <br>

   ```bash
   docker build -t my-fastapi-app .
   ```
    <br>

   Replace "my-fastapi-app" with the desired image name.
    <br>
    - **Run the Docker Container:**
   Run the Docker container based on the image you just built.
    <br>

   ```bash
   docker run -p 8000:8000 my-fastapi-app
   ```
    <br>
   This assumes your FastAPI application is set to run on port 8000.
<br>

Here's the complete Dockerfile:
<br>

```Dockerfile
FROM python:3.9

WORKDIR /app

COPY . /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
<br><br><br>

# Then create docker-compose.yml file:

```dockerfile
version: '3'
services:
  api:
    build: . 
    container_name: "restapi_fastapi"
    ports:
      - "8000:8000"
    volumes:
      - .:/app

```
<br> <br> <br>

# "gpg: public key decryption failed" error: 

<br>

The error message **"gpg: public key decryption failed"** indicates that `GPG (GNU Privacy Guard)` is having trouble decrypting or accessing the public key, possibly due to a missing or incorrect passphrase. In the context of Docker and the error you're encountering, GPG is used to sign and verify Docker images.

<br>

**Docker Content Trust (DCT)** is a security feature in Docker that uses GPG to sign and verify images. When you build or pull Docker images, Docker verifies the signature of the image using GPG. If the GPG key is not available or cannot be decrypted, you may encounter issues, as seen in your error message.


<br><br>

# Create a new **gpg** key by the below command: 


## GPG Key Generation

```bash
gpg --full-generate-key
```

### Key Selection
Please select what kind of key you want:
   - (1) RSA and RSA

### Key Size
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (3072) 1024

### Key Expiration
Please specify how long the key should be valid.
   - 0 = key does not expire
   - <n>  = key expires in n days
   - <n>w = key expires in n weeks
   - <n>m = key expires in n months
   - <n>y = key expires in n years
Key is valid for? (0) 1w

### Key User Identification
Real name: Yasin Arafat
Email address: yasinarafat.e2021@gmail.com
Comment: fastapi_docker

You selected this USER-ID:
   "Yasin Arafat (fastapi_docker) <yasinarafat.e2021@gmail.com>"

### Confirmation
Is this correct? (y/N) y

### Random Bytes Generation
We need to generate a lot of random bytes. It is a good idea to perform some other action (type on the keyboard, move the mouse, utilize the disks) during the prime generation; this gives the random number generator a better chance to gain enough entropy.

### Revocation Certificate
gpg: revocation certificate stored as '/home/yasin/.gnupg/openpgp-revocs.d/821EC292D64FC2BEDDF3824C94B3AB6F724AA812.rev'

### Key Information
- **Public Key:** rsa1024 2024-03-05 [SC] [expires: 2024-03-12]
  - 821EC292D64FC2BEDDF3824C94B3AB6F724AA812

- **User ID:** Yasin Arafat (fastapi_docker) <yasinarafat.e2021@gmail.com>

- **Sub Key:** rsa1024 2024-03-05 [E] [expires: 2024-03-12]


<br> <br> <br>

# **Get the newtwork Information of Docker:**

`Networking configuration in Docker is responsible for defining how containers communicate with each other and with the external world. It plays a crucial role in enabling communication between containers, connecting containers to specific networks, and exposing or publishing container ports to the host machine or external networks.`

```dockerfile

docker ps

docker inspect <container_name_or_id>

```
`docker ps` -> The docker ps command lists the containers that are running on your our current host.
<br>

`docker inspect` -> give all information about the docker image. <br>

`In the last section we will see the networking option.`
<br>

Let's break down the information in the "Networks" section of the `docker inspect` output and discuss the real-life implications of each term:

1. **Network Name (`rest_api_fastapi_default`):**
   - **Real-Life Analogy:** Think of it as a virtual network or a subnet within your Docker environment.
   - **Example:** You have multiple services running in Docker, and each service might be connected to a different network for isolation.

2. **Aliases (`fastapi_restapi`, `api`, `879ee690509f`):**
   - **Real-Life Analogy:** Aliases are like additional names or nicknames for a person.
   - **Example:** The container can be referred to by different names within the network, allowing services to communicate using different identifiers.

3. **MacAddress (`02:42:ac:12:00:02`):**
   - **Real-Life Analogy:** Similar to a physical device's MAC address, which is a unique identifier for network communication.
   - **Example:** Each network interface card (NIC) in your computer has a unique MAC address for identification on a network.

4. **NetworkID and EndpointID:**
   - **NetworkID:** Identifies the Docker network.
   - **EndpointID:** Identifies the specific container endpoint in the network.
   - **Real-Life Analogy:** Think of NetworkID as a street name, and EndpointID as the address on that street.
   - **Example:** In a city, multiple buildings (containers) can exist on the same street (network), each with a unique address (endpoint).

5. **Gateway (`172.18.0.1`):**
   - **Real-Life Analogy:** Similar to a gateway or router that connects different networks.
   - **Example:** In your home network, the router serves as the gateway connecting your local devices to the internet.

6. **IPAddress (`172.18.0.2`) and IPPrefixLen (`16`):**
   - **Real-Life Analogy:** Like a postal address, specifying the exact location of the container in the network.
   - **Example:** In a city, each building (container) has a unique street address (IP address), and the prefix length indicates the size of the address space.

7. **IPv6Gateway, GlobalIPv6Address, GlobalIPv6PrefixLen:**
   - **IPv6** equivalents of the above IPv4-related properties, relevant for IPv6 addressing.
   - **Example:** In a future scenario where IPv6 is widely used, these properties would provide the corresponding IPv6 details.

8. **DriverOpts:**
   - **Real-Life Analogy:** Configuration options specific to the network driver.
   - **Example:** If you use a custom network driver, there might be specific options or settings associated with it.

