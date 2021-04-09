# Created by ericc at 4/6/2021
Feature: Open Product and check for descriptions
  # Enter feature description here

  Scenario: Product is selected and Description is seen (iPad)
    Given Open iPad Gettop product page
    Then Verify description is available

  Scenario: Product is selected and Description is seen (Macbook)
    Given Open Macbook-Pro-13 Gettop product page
    Then Verify description is available

  Scenario: Product is selected and Description is seen (Airpods)
    Given Open airpods Gettop product page
    Then Verify description is available

  Scenario: Product is selected and Description is seen (Watch)
    Given Open ss-crew-california-sub-river-island Gettop product page
    Then Verify description is available

  Scenario: Product is selected and Description is seen (iPhone)
    Given Open iPhone-11 Gettop product page
    Then Verify description is available
