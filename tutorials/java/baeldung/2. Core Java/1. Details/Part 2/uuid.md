#### UUID in Java

    https://www.baeldung.com/java-uuid

- UUID (Universally Unique Identifier), also known as GUID (Globally Unique Identifier)
    - Represnts a 128-bit long value that is unique for all practical purposes
    - Standard representation of the UUID uses hex digits
- UUID is made up of hex digits along with 4 "-" symbols which make its length equal to 36 characters
    - The Nil UUID is a special form of UUID in which all bits are set to zero

UUID Class
- Have a single constructor, we need to provide two long values

        UUID uuid = new UUID(long mostSignificant64Bits, long leastSignificant64Bits)

        // Three static methods to generate UUID
        UUID uuid = UUID.nameUUIDFromBytes(byte[] bytes);
        UUID uuid = randomUUID(); //v3
        UUID uuid = UUID.fromString(String uuidHexDigitString); //v4

Structure
- Example UUID

        123e4567-e89b-42d3-a456-556642440000
        xxxxxxxx-xxxx-Bxxx-Axxx-xxxxxxxxxxxx

- UUID Variant: Most significant bit of "A" determines variant of UUID
    - 'a' = 10XX shows the variant 2
- UUID Version: B represents the version
- Get variant and version:

        UUID uuid = UUID.randomUUID();
        int variant = uuid.variant();
        int version = uuid.version();

Version
- V1: based on current timestamp
- V2: Based on timestamp and the Mac address
- V3: Generated using hash of namespace (DNS, OIDs, URLs etc.) and name
    - V5: Same as V3 with different hashing algorithm
- V4: Uses random numbers as the source.

When to use UUID
        https://stackoverflow.com/questions/703035/when-are-you-truly-forced-to-use-uuid-as-part-of-the-design